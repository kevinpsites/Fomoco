from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.http import HttpResponseRedirect


@view_function
def process_request(request, productid:cmod.Product):

    if not request.user.has_perm('auth.manager_view'):
        return HttpResponseRedirect('/homepage/index')
		
    productid.status = 'I'
    productid.save()

    return HttpResponseRedirect('/manager/ProductList')
