from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):


    context = {


    }

    return request.dmp.render('thanks.html', context)
