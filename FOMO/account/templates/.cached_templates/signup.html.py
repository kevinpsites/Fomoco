# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522968886.896589
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/account/templates/signup.html'
_template_uri = 'signup.html'
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
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="center">\n  <h1>Sign Up</h1>\n</div>\n\n<br />\n<div class="cent">\n  <div class="shrink">\n    ')
        __M_writer(str(form))
        __M_writer('\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/account/templates/signup.html", "uri": "signup.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 14, "48": 3, "55": 3, "56": 11, "57": 11, "63": 57}}
__M_END_METADATA
"""
