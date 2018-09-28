from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django.http import HttpResponseRedirect


@view_function
def process_request(request):

    cart = request.user.get_shopping_cart()
    cart.recalculate()
    items = cart.active_items(include_tax_item=False)
    taxline = cmod.OrderItem.objects.filter(order= cart, product__name="Sales Tax",status="active").first()
    total=cart.total_price
    total = round(total,2)
    context = {

    'items':items,
    'tax':taxline,
    'total':total
    }

    return request.dmp.render('cart.html', context)


@view_function
def delete(request, id:cmod.OrderItem=None):
    id.status="deleted"
    id.save()

    context = {


    }

    return HttpResponseRedirect('/catalog/cart/')
