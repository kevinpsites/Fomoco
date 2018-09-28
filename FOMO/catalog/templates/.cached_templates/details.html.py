# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523305663.58899
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/details.html'
_template_uri = 'details.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['top', 'center']


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
        pictures = context.get('pictures', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>')
        __M_writer(filters.html_escape(str(product.name )))
        __M_writer('</h1>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pictures = context.get('pictures', UNDEFINED)
        def center():
            return render_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<br />\n<br />\n<div id="contents">\n\n  <ul id="list-o-pics">\n')
        for item in pictures:
            __M_writer('\n      <li >\n        <div class="jq">\n          <img class="lil_img" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('/catalog/media/products/')
            __M_writer(str(item.filename))
            __M_writer('"/ alt="')
            __M_writer(str(item.filename))
            __M_writer('" >\n\n        </div>\n      </li>\n')
        __M_writer('  </ul>\n  <img id="big_image" src=')
        __M_writer(str(product.image_url()))
        __M_writer(' alt="')
        __M_writer(str(product.name))
        __M_writer('" >\n  <div class="disc">\n    <p>\n      <b>Price: $')
        __M_writer(str(product.price))
        __M_writer('</b>\n      ')
        __M_writer(str(product.description))
        __M_writer('\n    </p>\n\n\n\n')
        if product.get_quantity() == 0:
            __M_writer(' <p>\n   <strong>')
            __M_writer(str(product.name))
            __M_writer('s are currently out of stock. Please try back later.</strong>\n </p>\n')
        elif product.status=="I":
            __M_writer(' <p>\n   <strong>This item has been sold</strong>\n </p>\n')
        else:
            __M_writer(' <div class="endline">\n            ')
            __M_writer(str(form))
            __M_writer('\n</div>\n')
        __M_writer('\n\n\n  </div>\n\n</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 6, "52": 55, "58": 3, "65": 3, "66": 4, "67": 4, "73": 8, "83": 8, "84": 14, "85": 15, "86": 18, "87": 18, "88": 18, "89": 18, "90": 18, "91": 18, "92": 23, "93": 24, "94": 24, "95": 24, "96": 24, "97": 27, "98": 27, "99": 28, "100": 28, "101": 33, "102": 34, "103": 35, "104": 35, "105": 37, "106": 38, "107": 41, "108": 42, "109": 43, "110": 43, "111": 46, "117": 111}}
__M_END_METADATA
"""
