# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520281731.0128992
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/manager/templates/ProductList.html'
_template_uri = 'ProductList.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content']


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
        List = context.get('List', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        List = context.get('List', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n<h2>Product List</h2>\n<a href="/manager/createProduct" type="button" class="btn btn-primary">Create New Product</a>\n\n<table class="table table-striped">\n<thead>\n  <tr>\n    <th>Category</th>\n    <th>Product Type</th>\n    <th>Name</th>\n    <th>Price</th>\n    <th>Quantity</th>\n    <th></th>\n  </tr>\n</thead>\n<tbody>\n')
        for item in List:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(item.category))
            __M_writer('</td>\n    <td>')
            __M_writer(str(item.TITLE))
            __M_writer('</td>\n    <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n    <td>$ ')
            __M_writer(str(item.price))
            __M_writer('</td>\n    <td>')
            __M_writer(str(item.get_quantity()))
            __M_writer('</td>\n    <td><a href="/manager/editProduct/')
            __M_writer(str(item.id))
            __M_writer('">Edit</a> | <a href="/manager/deleteProduct/')
            __M_writer(str(item.id))
            __M_writer('">Delete</a></td>\n  </tr>\n\n')
        __M_writer('\n</tbody>\n</table>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/manager/templates/ProductList.html", "uri": "ProductList.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 35, "48": 3, "55": 3, "56": 20, "57": 21, "58": 22, "59": 22, "60": 23, "61": 23, "62": 24, "63": 24, "64": 25, "65": 25, "66": 26, "67": 26, "68": 27, "69": 27, "70": 27, "71": 27, "72": 31, "78": 72}}
__M_END_METADATA
"""
