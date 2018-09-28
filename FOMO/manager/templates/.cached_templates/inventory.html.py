# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523412745.0800698
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/manager/templates/inventory.html'
_template_uri = 'inventory.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content']


from catalog import models as cmod

from datetime import datetime,timedelta

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
    return runtime._inherit_from(context, '/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        lone = context.get('lone', UNDEFINED)
        bulk = context.get('bulk', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rent = context.get('rent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lone = context.get('lone', UNDEFINED)
        bulk = context.get('bulk', UNDEFINED)
        def content():
            return render_content(context)
        rent = context.get('rent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container">\n  <div class="center-fi">\n    <h1>Inventory</h1>\n  </div>\n\n<h2>Bulk Products to Restock</h2>\n\n<table id="left"class="table table-striped">\n<thead>\n  <tr>\n    <th>Name</th>\n    <th>Category</th>\n    <th>Quantity</th>\n    <th>Reorder Trigger</th>\n    <th>Refill Qty</th>\n    <th></th>\n  </tr>\n</thead>\n<tbody>\n')
        for item in bulk:
            if item.quantity <= item.reorder_trigger:
                __M_writer('  <tr>\n\n    <td>')
                __M_writer(str(item.name))
                __M_writer('</td>\n    <td>')
                __M_writer(str(item.category))
                __M_writer('</td>\n    <td>')
                __M_writer(str(item.get_quantity()))
                __M_writer('</td>\n    <td>')
                __M_writer(str(item.reorder_trigger))
                __M_writer('</td>\n    <td>')
                __M_writer(str(item.reorder_quantity))
                __M_writer('</td>\n    <td><a href="/manager/editProduct/')
                __M_writer(str(item.id))
                __M_writer('">Edit</a> | <a href="/manager/deleteProduct/')
                __M_writer(str(item.id))
                __M_writer('">Delete</a></td>\n\n  </tr>\n')
        __M_writer('</tbody>\n</table>\n</div>\n\n<div class="container">\n<h2>Outstanding Rentals</h2>\n\n<table class="table table-striped">\n<thead>\n  <tr>\n    <th>Name</th>\n    <th>Price</th>\n    <th>Renter\'s Email</th>\n    <th>Start Date</th>\n    <th>Return Date</th>\n    <th></th>\n  </tr>\n</thead>\n<tbody>\n')
        for item in rent:
            __M_writer('\n  <tr>\n\n    <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n    <td>$')
            __M_writer(str(item.price))
            __M_writer('</td>\n    <td>')
            __M_writer(str(cmod.OrderItem.objects.filter(product = item.id).last().order.user.email))
            __M_writer('</td>\n    <td>')
            __M_writer(str(cmod.OrderItem.objects.filter(product = item.id).last().order.order_date.date()))
            __M_writer('</td>\n    <td>')
            __M_writer(str(cmod.OrderItem.objects.filter(product = item.id).last().order.order_date.date() + timedelta(days=item.max_rental_days)))
            __M_writer('</td>\n    <td><a href="/manager/editProduct/')
            __M_writer(str(item.id))
            __M_writer('">Edit</a> | <a href="/manager/deleteProduct/')
            __M_writer(str(item.id))
            __M_writer('">Delete</a></td>\n  </tr>\n\n')
        __M_writer('\n</tbody>\n</table>\n</div>\n\n<!-- <div class="container">\n<h2>Individual Products Sold</h2>\n\n<table class="table table-striped">\n<thead>\n  <tr>\n\n    <th>Name</th>\n    <th>Price</th>\n    <th></th>\n  </tr>\n</thead>\n<tbody>\n')
        for item in lone:
            __M_writer('  <tr>\n\n    <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n    <td>$ ')
            __M_writer(str(item.price))
            __M_writer('</td>\n    <td><a href="/manager/editProduct/')
            __M_writer(str(item.id))
            __M_writer('">Edit</a> | <a href="/manager/deleteProduct/')
            __M_writer(str(item.id))
            __M_writer('">Delete</a></td>\n  </tr>\n\n')
        __M_writer('\n</tbody>\n</table>\n</div> -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/manager/templates/inventory.html", "uri": "inventory.html", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 3, "33": 0, "43": 1, "44": 2, "45": 3, "50": 102, "56": 4, "65": 4, "66": 25, "67": 26, "68": 27, "69": 29, "70": 29, "71": 30, "72": 30, "73": 31, "74": 31, "75": 32, "76": 32, "77": 33, "78": 33, "79": 34, "80": 34, "81": 34, "82": 34, "83": 39, "84": 58, "85": 59, "86": 62, "87": 62, "88": 63, "89": 63, "90": 64, "91": 64, "92": 65, "93": 65, "94": 66, "95": 66, "96": 67, "97": 67, "98": 67, "99": 67, "100": 71, "101": 89, "102": 90, "103": 92, "104": 92, "105": 93, "106": 93, "107": 94, "108": 94, "109": 94, "110": 94, "111": 98, "117": 111}}
__M_END_METADATA
"""
