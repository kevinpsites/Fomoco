from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from account import models as amod
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from decimal import Decimal
import math


@view_function
def process_request(request):
    print('hello')
    #category Use contains (LIKE query) and case insensitive
    #product Use contains (LIKE query) and case insensitive
    #max_price Return all matching products less or equal to the amount given
    #page Default to page 1.  Show only 6 results per page.

    # lname = 'Doe'
    # Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
    #SELECT table.id, other_table.name AS name from table join other_table using (id)

    pcategory = request.GET['category']
    pproduct = request.GET['product']
    pprice = request.GET['max_price']
    ppage = request.GET['page']
    ppage = (int(ppage)-1)

    # for p in cmod.Product.objects.raw('Select * FROM public.catalog_product where public.catalog_product.category_id = %s', [32] ):
    #     print('>>>>>>>>>>>>>>>>>', p.name)
    #
    # for p in cmod.Category.objects.raw('Select * FROM public.catalog_category where public.catalog_category.name = %s', [pcategory] ):
    #     print('>>>>>>>>>>>>>>>>> cat', p.name)
    products =[]
    listp = []
    for p in cmod.Product.objects.filter(category__name = pcategory, name__icontains=pproduct, price__lte=pprice ):
        products.append({'category__name': p.category.name, 'name': p.name, 'price': p.price})
        listp.append(p)

    allp = cmod.Product.objects.filter(category__name = pcategory, name__icontains=pproduct, price__lte=pprice )
    pcount = allp.count()

    #divide by 6 to get the number of pages the category has
    pcount = math.ceil(pcount/6)

    productc = []

    productc = allp[(ppage*6):(ppage+1)*6]

    productc2 = []
    for p in productc:
        productc2.append({'category__name': p.category.name, 'name': p.name, 'price': p.price})

    productsf ={'Products':productc2}

    print('broken')
    return JsonResponse(productsf, safe=False)
