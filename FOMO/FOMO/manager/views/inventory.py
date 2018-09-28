from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):
    if not request.user.has_perm('auth.manager_view'):
        return HttpResponseRedirect('/homepage/index')
    bulk = cmod.BulkProduct.objects.all()
    rent = cmod.RentalProduct.objects.filter(status="I")
    lone = cmod.IndividualProduct.objects.filter(status="I")

    context = {
        # sent to index.html:
        'bulk': bulk,
        'rent': rent,
        'lone': lone,
        # sent to index.html and index.js:

    }
    return request.dmp.render('inventory.html', context)
