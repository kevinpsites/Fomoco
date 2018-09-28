from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from account import models as amod
from django.contrib.auth import authenticate, login
import re

@view_function
def process_request(request):

    form = SignUpForm(request)

    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/homepage/index')
    form.submit_text="Sign Up"
#render the format
    context = {
        'form': form,

    }
    return request.dmp.render('signup.html',context)


class SignUpForm(Formless):
    def init(self):

        self.fields['first_name'] = forms.CharField(label='First Name', max_length=100)
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['birthdate'] = forms.DateField(label='Birthday',)
        self.fields['address'] = forms.CharField(label='Address',)
        self.fields['city'] = forms.CharField(label='City')
        self.fields['state'] = forms.CharField(label='State')
        self.fields['zipcode'] = forms.CharField(label='Zipcode')
        self.fields['email']=forms.EmailField(label='Your Email')
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())



    def clean_email(self):
        email = self.cleaned_data.get('email')
        account = amod.User.objects.filter(email__iexact=email).count()
        if account > 0:
            raise forms.ValidationError("This email already exists")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",password) is None:
            raise forms.ValidationError('Your password must contain a number and be at least 8 characters')
        return password

    def clean(self):
        if not self.errors:
            password1 = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('password2')

            if password1 != password2:
                raise forms.ValidationError("Your passwords don't match")
        return self.cleaned_data

    def commit(self):
        user = amod.User()
        user.email= self.cleaned_data.get('email')
        user.first_name= self.cleaned_data.get('first_name')
        user.last_name= self.cleaned_data.get('last_name')
        user.address = self.cleaned_data.get('address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.birthdate = self.cleaned_data.get('birthdate')
        user.set_password(self.cleaned_data.get('password'))
        print('>>>>>>>>>>>>>> Is this even working?!')
        user.save()

        user2 = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        print('>>>>>>>>>> >>>>>>>>>>',user2,user)
        login(self.request, user2)
