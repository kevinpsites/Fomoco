# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522971754.3953972
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/cart.html'
_template_uri = 'cart.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tax = context.get('tax', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
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
        tax = context.get('tax', UNDEFINED)
        def center():
            return render_center(context)
        items = context.get('items', UNDEFINED)
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<br />\n<br />\n<div >\n\n\n<table class="table table-bordered">\n    <thead>\n      <tr>\n        <th>Product</th>\n        <th>Price</th>\n        <th>Quantity</th>\n        <th>Subtotal</th>\n        <th></th>\n      </tr>\n    </thead>\n    <tbody>\n')
        for item in items:
            __M_writer('      <tr>\n        <td>\n          ')
            __M_writer(str(item.product.name))
            __M_writer('\n        </td>\n        <td>\n          ')
            __M_writer(str('${:,.2f}'.format(item.price)))
            __M_writer('\n        </td>\n        <td>\n          ')
            __M_writer(str(item.quantity))
            __M_writer('\n        </td>\n        <td>\n          ')
            __M_writer(str('${:,.2f}'.format(item.extended)))
            __M_writer('\n        </td>\n\n        <td>\n')
            if item.product.name != "Sales Tax":
                __M_writer('            <a class = "del" href="/catalog/cart.delete/')
                __M_writer(str(item.id))
                __M_writer('"> <span class="glyphicon glyphicon-remove"></span> Delete</a>\n')
            __M_writer('        </td>\n\n      </tr>\n')
        __M_writer('\n    </tbody>\n  </table>\n</div>\n<div class = "right">\n  <table class="table table-hover">\n\n    <tbody>\n      <tr>\n\n        <td>')
        __M_writer(str(tax.product.name))
        __M_writer('</td>\n        <td> ')
        __M_writer(str('${:,.2f}'.format(tax.price)))
        __M_writer('</td>\n        <td></td>\n      </tr>\n      <tr>\n\n        <td>Total Price:</td>\n        <td>')
        __M_writer(str('${:,.2f}'.format(total)))
        __M_writer('</td>\n        <td></td>\n      </tr>\n\n    </tbody>\n  </table>\n</div>\n\n<div class="right">\n  <a href=\'/catalog/checkout/\'><button type="button" class="btn btn-info pull-right">Checkout</button></a>\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 72, "50": 2, "59": 2, "60": 19, "61": 20, "62": 22, "63": 22, "64": 25, "65": 25, "66": 28, "67": 28, "68": 31, "69": 31, "70": 35, "71": 36, "72": 36, "73": 36, "74": 38, "75": 42, "76": 52, "77": 52, "78": 53, "79": 53, "80": 59, "81": 59, "87": 81}}
__M_END_METADATA
"""
