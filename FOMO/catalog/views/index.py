from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
import math

@view_function
def process_request(request, category:cmod.Category=None):


    cats = cmod.Category.objects.all()
    name = "All Products"
    if category is not None:
        name = category.name

    qry = cmod.Product.objects.filter(status="A").exclude(name="Sales Tax")
    if category is not None:
        qry = qry.filter(category=category.id)
    pages = math.ceil(qry.count()/6)
    print(qry.count())
    print(pages,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    context = {
        # sent to index.html:

    'cats': cats,
    'name': name,
    'pages': pages,
    jscontext('cat'):category.id if category is not None else 0,
    jscontext('maxpage'):pages
        # sent to index.html and index.js:

    }
    return request.dmp.render('index.html', context)


@view_function
def products(request, cat:cmod.Category=None, Pnum:int=0):
    qry = cmod.Product.objects.filter(status="A").exclude(name="Sales Tax")
    if cat is not None:
        qry = qry.filter(category=cat.id)
    qry = qry[Pnum * 6:(Pnum+1) * 6]

    context = {
        'qry':qry,
        jscontext('cat'):cat.id if cat is not None else 0,
        jscontext('Page'):Pnum,
    }


    return request.dmp.render('index.products.html',context)
