# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523412418.5769129
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/faq.html'
_template_uri = 'faq.html'
_source_encoding = 'utf-8'
import django_mako_plus
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
        def center():
            return render_center(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def maintain():
            return render_maintain(context._locals(__M_locals))
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
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n<h1 class="top">Frequently Asked Questions</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n<div>\n<h4>What does FOMO stand for?</h4>\n<p>FOMO stand for "Fear Of Missing Out", but in this case it actually\n  stands for "Family Oriented Music Organization". Thats because our focus is on\n  getting musical instruments into peoples homes and bringing families together through\n  a shared love of music.\n</p>\n</div>\n<div>\n<h4>What kind of instruments do you sell?</h4>\n<p>We sell all types of instruments, from triangles all the way up to didgeridoo. Anything you can think\n  of we have it. And if we don\'t, we will find it for you.\n</p>\n</div>\n\n<div>\n<h4>Where is your store located?</h4>\n<p>\n  We have three locations one on Main Street in SLC, another on Center Street in Provo, and we recently opened a store in Dubai.\n</p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/faq.html", "uri": "faq.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 5, "54": 9, "59": 13, "64": 37, "69": 41, "75": 3, "81": 3, "87": 7, "93": 7, "99": 11, "105": 11, "111": 15, "117": 15, "123": 39, "129": 39, "135": 129}}
__M_END_METADATA
"""
