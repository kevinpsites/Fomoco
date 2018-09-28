from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django import forms
from formlib.form import Formless
from django.http import HttpResponseRedirect
from account import models as amod

@view_function
def process_request(request, product:cmod.Product=None):
    print(product,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if product is None:
        return HttpResponseRedirect('/catalog/index')

    picList = product.image_urls().order_by('id')
    for p in picList:
        print(p.filename)
    type = product.TITLE
    quant = product.get_quantity();
    name = cmod.Category.objects.get(id = product.category_id).name
    user = request.user

    if product in request.last_five:
        request.last_five.remove(product)

    request.last_five.insert(0,product)

    if len(request.last_five) > 6:
        request.last_five.pop()

    form = BuyForm(request, prod=product)
    if form.is_valid():
        if request.user.is_authenticated != True:
            return HttpResponseRedirect('/account/login')

        form.commit(product)
        return HttpResponseRedirect('/catalog/cart')
    form.submit_text = 'Add to Cart'

    context = {
        # sent to index.html:
        'form': form,
        'quant':quant,
        'type':type,
        'product': product,
        'name': name if name is not None else "All Products",
        'catID': product.category,
        'pictures':picList,
        # sent to index.html and index.js:

    }
    return request.dmp.render('details.html', context)

class BuyForm(Formless):
    def init(self):
        if self.request.user.is_authenticated:
            self.cart = self.request.user.get_shopping_cart()
        quanty = []
        for x in range(1,self.prod.get_quantity()+1):
            quanty.append([str(x),str(x)])
        # self.fields['Quantity'] = forms.IntegerField(label="quant", max_value= self.quant)

        if self.prod.TITLE == "Bulk":
            self.fields['quantity']= forms.ChoiceField(choices=quanty)
        else:
            self.fields['quantity']=forms.CharField(initial=1, widget=forms.HiddenInput)

    def commit(self, product):
        item = self.cart.get_item(product, True)
        q = int(self.cleaned_data.get('quantity'))
        item.recalculate(q)

    def clean(self):
        if self.request.user.is_authenticated != True:
            return HttpResponseRedirect('/account/login')
        quantity = self.cleaned_data.get('quantity')
        quantity = int(quantity)
        item = self.cart.get_item(self.prod,True)
        item.recalculate(0)
        if item is not None:
            if item.quantity + quantity > self.prod.get_quantity():
                if self.prod.TITLE == "Bulk":
                    raise forms.ValidationError("You can only order " + str(self.prod.get_quantity()) +" "+ self.prod.name +"s. You currently have "+str(item.quantity)+ " in your cart.")
                else:
                    raise forms.ValidationError("This item is already in your cart")

        return self.cleaned_data
