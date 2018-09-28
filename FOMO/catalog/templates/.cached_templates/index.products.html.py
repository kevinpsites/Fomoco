# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523218866.7806458
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/index.products.html'
_template_uri = 'index.products.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        qry = context.get('qry', UNDEFINED)
        __M_writer = context.writer()
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
        def content():
            return render_content(context)
        qry = context.get('qry', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<ul id="pic_list">\n')
        for item in qry:
            __M_writer('\n    <li >\n      <a href="/catalog/details/')
            __M_writer(str(item.id))
            __M_writer('">\n      <div class="tile">\n        <img src=')
            __M_writer(str(item.image_url()))
            __M_writer(' alt="')
            __M_writer(str(item.name))
            __M_writer('" >\n        <br />\n        <div class="nm text-center">\n          ')
            __M_writer(str(item.name))
            __M_writer('\n          \n          <br />\n        </div>\n        <div class="price">\n          $')
            __M_writer(str(item.price))
            __M_writer('\n        </div>\n      </div>\n      </a>\n    </li>\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/catalog/templates/index.products.html", "uri": "index.products.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 24, "48": 2, "55": 2, "56": 4, "57": 5, "58": 7, "59": 7, "60": 9, "61": 9, "62": 9, "63": 9, "64": 12, "65": 12, "66": 17, "67": 17, "68": 23, "74": 68}}
__M_END_METADATA
"""
