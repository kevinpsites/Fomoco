# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521095092.5328152
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/manager/templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        utc_time = context.get('utc_time', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        utc_time = context.get('utc_time', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\n        <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.</h4>\n        <h4 class="utc-time">Current time in UTC: ')
        __M_writer(str( utc_time ))
        __M_writer('</h4>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/manager/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "47": 3, "54": 3, "55": 7, "56": 7, "62": 56}}
__M_END_METADATA
"""
