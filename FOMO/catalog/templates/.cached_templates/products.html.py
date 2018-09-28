# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520388213.01572
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['left', 'top', 'center']


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
    return runtime._inherit_from(context, 'homepage/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        cat = context.get('cat', UNDEFINED)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat = context.get('cat', UNDEFINED)
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<ul id="product_list" class="nav  nav-pills nav-stacked">\n  <li>\n    <a href="/catalog/products/" type="button" class="btn btn-primary nav-item category_nav">All Products</a>\n  </li>\n')
        for item in cat:
            __M_writer('  <li>\n\n    <a href="/catalog/products/')
            __M_writer(str(item.name))
            __M_writer('" type="button" class="btn btn-primary nav-item category_nav">')
            __M_writer(str(item.name))
            __M_writer('</a>\n  </li>\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        name = context.get('name', UNDEFINED)
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n  <h1>')
        __M_writer(str(name))
        __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n  <div id=Ajax>\n    \n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/products.html", "uri": "products.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 14, "52": 19, "57": 25, "63": 2, "70": 2, "71": 7, "72": 8, "73": 10, "74": 10, "75": 10, "76": 10, "77": 13, "83": 17, "90": 17, "91": 18, "92": 18, "98": 21, "104": 21, "110": 104}}
__M_END_METADATA
"""
