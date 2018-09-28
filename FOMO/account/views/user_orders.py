from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from account import models as amod
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if request.user.is_authenticated != True:
        return HttpResponseRedirect('/account/login')
    orders = cmod.Order.objects.filter(user=request.user).filter(status="sold").order_by('-id')

    context = {
    'orders':orders,
    'user':request.user,
    }
    return request.dmp.render('user_orders.html', context)
