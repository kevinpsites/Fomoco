from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function
def process_request(request,category):
    cat = cmod.Category.objects.all()
    name = "All Products"
    for c in cat:
        if category == c.name:
            name = c.name

    context = {
        # sent to index.html:
    'cat': cat,
    'name': name
        # sent to index.html and index.js:

    }
    return request.dmp.render('products.html', context)
