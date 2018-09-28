from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect
from formlib import Formless
from django import forms
from django.core.mail import send_mail

@view_function
def process_request(request):

    form = ContactForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/homepage/index')
    form.submit_text="Send"

    context = {
    'form': form
    }
    return request.dmp.render('contact.html', context)


class ContactForm(Formless):
    def init(self):

        self.fields['first_name'] = forms.CharField(label='First Name', max_length=100)
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['email']=forms.EmailField(label='Your Email')
        self.fields['message']=forms.CharField(label="Your Message",widget=forms.Textarea)

    def commit(self):
        name = self.cleaned_data.get('first_name') + ' ' + self.cleaned_data.get('last_name')
        Customer_Email = "User's name: " + name + "; email: " +self.cleaned_data.get('email')+ "; Message: " + self.cleaned_data.get('message')
        print(Customer_Email)

        send_mail(
            subject='Message from '+ name,
            message=Customer_Email,
            from_email='receipt@fomoco.me',
            recipient_list=['receipt@fomoco.me'],
            fail_silently=False,



        )
