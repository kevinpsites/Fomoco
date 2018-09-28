from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from formlib import Formless
from django import forms
from account import models as amod
import re
from ldap3 import Server, Connection, ALL, SUBTREE, ALL_ATTRIBUTES
from ldap3.utils.conv import escape_bytes
from django.contrib.auth.models import Permission, Group, ContentType

@view_function
def process_request(request):

    form = LoginForm(request)

    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/homepage/index')
    form.submit_text="Login"
    return request.dmp.render('login.html',{
    'form': form,
    })

class LoginForm(Formless):
    def init(self):

        self.fields['email'] = forms.CharField(label='Email Address')
        self.fields['password'] = forms.CharField(label="Password", widget=forms.PasswordInput())
        self.user = None

    def clean(self):
        #try to log in from FOMO User database else try AD
        try:
            print('ad start')
            username = self.cleaned_data.get('email')
            # if all checks out then do the work (authenticate and login)
            #authenticate the user in AD first
            filter = '(userPrincipalName=%s)' % (username+"@fomoco.local")
            s = Server(host = '172.20.22.218', port=389, use_ssl=False, get_info='ALL')
            c= Connection(s, user=("fomoco\\"+self.cleaned_data.get('email')), password=self.cleaned_data.get('password'))
            if not c.bind():
                print('no bind')
                self.user = authenticate(username=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
                if self.user is None:
                    raise forms.ValidationError('Invalid username or password')
            else:
                try:
                    print('query')
                    user = amod.User.objects.get(email=username)
                except: user = amod.User()

                print('ad search')
                print('user pre', user)

                c.search('CN=Users, dc=fomoco, dc=local', filter , SUBTREE, attributes=ALL_ATTRIBUTES)
                ldap_user = c.response[0]['attributes']
                ##Change the username if the AD record has one
                if ldap_user['userPrincipalName']:
                    u = user
                    u.email = ldap_user['sAMAccountName']
                    u.save()
                    print('u', u)
                    print('email', u.email)
                ##update the user's first name
                try:
                    ldap_user['givenName']
                    u = user
                    u.first_name = ldap_user['givenName']
                    u.save()
                except: u.first_name = ''
                ##update the user's last name
                try:
                    ldap_user['sn']
                    u = user
                    u.last_name = ldap_user['sn']
                    u.save()
                except: u.last_name = ''

                ##update the password & save again
                u = user
                u.set_password(self.cleaned_data.get('password'))

                #add auth.manager_view permission to ad users
                p = Permission.objects.filter(codename='manager_view').first()
                u.user_permissions.add(p)

                u.save()

        except:
            self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
            if self.user is None:
                print('>>>>>', self.user)
                raise forms.ValidationError('Invalid3 username or password')

        self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        return self.cleaned_data

    def commit(self):
        login(self.request, self.user)
