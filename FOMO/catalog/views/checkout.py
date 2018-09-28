from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.http import HttpResponseRedirect
from django import forms
from formlib.form import Formless
from django.core.mail import send_mail
from django.template.loader import render_to_string


@view_function
def process_request(request):

    cart = cmod.Order.objects.get(user=request.user,status='cart')
    cart.recalculate()
    taxi = cmod.OrderItem.objects.filter(order= cart, product__name="Sales Tax",status="active").first()
    items= cart.active_items(include_tax_item=False)
    total=cart.total_price
    total= '${:,.2f}'.format(total)
    # total = round(total,2)
    ship={}
    ship['city'] = request.user.city
    ship['shipping_address'] = request.user.address
    ship['state'] = request.user.state
    ship['zip_code'] = request.user.zipcode
    form = CheckoutForm(request,initial=ship,cart=cart)
    form.submit_text=None
    if form.is_valid():
        form.commit(cart.id,taxi,items )
        return HttpResponseRedirect('/catalog/thanks')
    context = {
        'form':form,
        'cart':cart,
        'total':total,


        }

    return request.dmp.render('checkout.html', context)

class CheckoutForm(Formless):
    def init(self):

        self.fields['shipping_address'] = forms.CharField()
        self.fields['city'] = forms.CharField()
        self.fields['state'] = forms.CharField()
        self.fields['zip_code'] = forms.CharField()
        self.fields['stripeToken']= forms.CharField(required=True,label="stripeToken", widget=forms.HiddenInput)

    def clean(self):
        try:
            self.cart.finalize(self.cleaned_data.get('stripeToken'))

        except Exception as E:
            raise forms.ValidationError(str(E))

        return self.cleaned_data

    def commit(self, cart, taxi, items):
        crt = cmod.Order.objects.get(id = cart)
        crt.ship_address =self.cleaned_data.get('shipping_address')
        crt.ship_city = self.cleaned_data.get('city')
        crt.ship_state = self.cleaned_data.get('state')
        crt.ship_zip_code = self.cleaned_data.get('zip_code')
        crt.save()
        UN = crt.user.email
        if '@' not in UN:
            UN = UN + '@fomoco.me'
        print(UN)
        msg_html = render_to_string('catalog/email_receipt.html', {'user': crt.user, 'order':crt, 'items':items,'tax':taxi})
        send_mail(
            subject='FOMO order receipt',
            message='Here is the message.',
            from_email='receipt@fomoco.me',
            recipient_list=[UN],
            fail_silently=True,
            html_message=msg_html,


        )
