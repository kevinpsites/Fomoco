# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523409678.8997
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['menu']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def menu():
            return render_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n      <li class="')
        __M_writer(str('active' if request.dmp.page == 'index'and request.dmp.app == 'homepage' else ''))
        __M_writer('"><a href="/homepage/index/">Home</a></li>\n      <li class="')
        __M_writer(str('active' if request.dmp.app == 'catalog' else ''))
        __M_writer('"><a href="/catalog/index">Catalog</a></li>\n      <li class="')
        __M_writer(str('active' if request.dmp.page == 'about' else ''))
        __M_writer('"><a href="/homepage/about/">About</a></li>\n      <li class="')
        __M_writer(str('active' if request.dmp.page == 'contact' else ''))
        __M_writer('"><a href="/homepage/contact/">Contact</a></li>\n      <li class="')
        __M_writer(str('active' if request.dmp.page == 'terms' else ''))
        __M_writer('"><a href="/homepage/terms/">Terms</a></li>\n      <li class="')
        __M_writer(str('active' if request.dmp.page == 'faq' else ''))
        __M_writer('"><a href="/homepage/faq/">FAQ</a></li>\n      <!-- <li class="')
        __M_writer(str('active' if request.dmp.page == 'sections' else ''))
        __M_writer('"><a href="/homepage/sections/">Sections</a></li> -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 13, "48": 4, "55": 4, "56": 5, "57": 5, "58": 6, "59": 6, "60": 7, "61": 7, "62": 8, "63": 8, "64": 9, "65": 9, "66": 10, "67": 10, "68": 11, "69": 11, "75": 69}}
__M_END_METADATA
"""
