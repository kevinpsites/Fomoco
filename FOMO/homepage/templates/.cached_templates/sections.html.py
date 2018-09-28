# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516657972.455101
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['maintain', 'top', 'left', 'center', 'right']


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
        def top():
            return render_top(context._locals(__M_locals))
        def maintain():
            return render_maintain(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintain'):
            context['self'].maintain(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintain(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintain():
            return render_maintain(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class = "maint">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\n    tempor incididunt ut labore et dolore magna aliqua.</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "top">Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit, sed do eiusmod\n  tempor incididunt ut labore et dolore magna aliqua.\n  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\n   in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\n   cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "lefty">Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit, sed do eiusmod\n  tempor incididunt ut labore et dolore magna aliqua.\n  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\n   in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\n   cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est.</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "middy">Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit, sed do eiusmod\n  tempor incididunt ut labore et dolore magna aliqua.\n  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\n   in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\n   cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n   Lorem ipsum dolor sit amet,\n     consectetur adipiscing elit, sed do eiusmod\n     tempor incididunt ut labore et dolore magna aliqua.\n     Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n     nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\n      in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\n      cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est.</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        __M_writer('\n<div class = "righty">Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit, sed do eiusmod\n  tempor incididunt ut labore et dolore magna aliqua.\n  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n  nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit\n   in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\n   cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est.</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/sections.html", "uri": "sections.html", "source_encoding": "utf-8", "line_map": {"28": 0, "43": 1, "48": 6, "53": 16, "58": 26, "63": 43, "68": 53, "74": 3, "80": 3, "86": 8, "92": 8, "98": 18, "104": 18, "110": 28, "116": 28, "122": 45, "128": 45, "134": 128}}
__M_END_METADATA
"""
