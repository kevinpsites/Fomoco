from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    if not request.user.has_perm('auth.manager_view'):
        return HttpResponseRedirect('/homepage/index')

		
    PList = cmod.Product.objects.filter(status='A').exclude(name="Sales Tax")

    context = {
        # sent to index.html:
        'List': PList,
        # sent to index.html and index.js:

    }
    return request.dmp.render('ProductList.html', context)
