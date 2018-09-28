# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523464883.2520347
_enable_loop = True
_template_filename = 'C:/Apache24/htdocs/FOMO/account/templates/user_orders.html'
_template_uri = 'user_orders.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['center']


from catalog import models as cmod

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        orders = context.get('orders', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        orders = context.get('orders', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if not orders:
            __M_writer('<div class="center-fi">\n  <h1>You Currently Have Zero Orders</h1>\n  <br />\n  <a class="btn btn-primary"href="/catalog/index">Click here to get one started</a>\n</div>\n\n')
        else:
            __M_writer('  <h1>Your Orders</h1>\n')
            for o in orders:
                __M_writer('  <div class="panel-group">\n  <div class="panel panel-default">\n    <div class="panel-heading">\n      <h4 class="panel-title">\n        <a id="title" data-toggle="collapse" href="#collapse')
                __M_writer(str(o.id))
                __M_writer('"><h2>Order #')
                __M_writer(str(o.id))
                __M_writer(' - Order Date: ')
                __M_writer(str(o.order_date.date()))
                __M_writer('</h2></a>\n      </h4>\n    </div>\n    <div id="collapse')
                __M_writer(str(o.id))
                __M_writer('" class="panel-collapse collapse">\n      <table class="ord table table-striped">\n        <thead>\n          <tr>\n            <th>Product</th>\n            <th>Price</th>\n            <th>Quantity</th>\n            <th>Item Total</th>\n            <th></th>\n          </tr>\n        </thead>\n        <tbody>\n')
                for i in o.active_items(include_tax_item=False):
                    __M_writer('\n\n      <tr>\n        <td>')
                    __M_writer(str(i.product.name))
                    __M_writer('</td>\n        <td>')
                    __M_writer(str(i.price))
                    __M_writer('</td>\n        <td>')
                    __M_writer(str(i.quantity))
                    __M_writer('</td>\n        <td>')
                    __M_writer(str(i.extended))
                    __M_writer('</td>\n\n      </tr>\n\n\n\n')
                __M_writer('        <tr id="end-row">\n          <td></td>\n          <td></td>\n          <td><strong>Tax</strong></td>\n          <td><strong>')
                __M_writer(str(o.get_item(product=cmod.Product.objects.filter(name="Sales Tax").first()).price))
                __M_writer('</strong></td>\n\n        </tr>\n        <tr id="end-row">\n\n          <td></td>\n          <td></td>\n          <td><strong>Total</strong></td>\n          <td><strong>')
                __M_writer(str(o.total_price))
                __M_writer('</strong></td>\n\n        </tr>\n      </tbody>\n    </table>\n\n\n    </div>\n  </div>\n</div>\n')
            __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Apache24/htdocs/FOMO/account/templates/user_orders.html", "uri": "user_orders.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "39": 1, "40": 2, "45": 74, "51": 3, "58": 3, "59": 4, "60": 5, "61": 11, "62": 12, "63": 13, "64": 14, "65": 18, "66": 18, "67": 18, "68": 18, "69": 18, "70": 18, "71": 21, "72": 21, "73": 33, "74": 34, "75": 37, "76": 37, "77": 38, "78": 38, "79": 39, "80": 39, "81": 40, "82": 40, "83": 47, "84": 51, "85": 51, "86": 59, "87": 59, "88": 70, "94": 88}}
__M_END_METADATA
"""
