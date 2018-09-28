from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless
from account import models as amod
from django.contrib.auth import logout

@view_function
def process_request(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')
