# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523545717.5153463
_enable_loop = True
_template_filename = 'C:/Apache24/htdocs/FOMO/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['maintain', 'top', 'left', 'content', 'right']


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
        def left():
            return render_left(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\n\n<!-- <div class=\'centered\'>\n  <button type="button" class="btn btn-primary">Primary</button>\n  <button type="button" class="btn btn-success">Success</button>\n  <button type="button" class="btn btn-info">Info</button>\n  <button type="button" class="btn btn-warning">Warning</button>\n  <button type="button" class="btn btn-danger">Danger</button>\n</div> -->\n')
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n<div class=" row black">\n\n<div class= "col-md-8 black">\n  <img class="imag" alt="Acoustic Guitar" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/acoustic.jpg">\n</div>\n  <div class= "col-md-4 black move">\n    <h1>Welcome to <br/>\n\n    <span class="bigtitle">FOMO</span></h1>\n\n    <br />\n\n    <a href="/catalog/index" type="button" class="btn btn-warning btn-color btn-lg">Buy Now</a>\n  </div>\n\n</div>\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<br />\n<h2 class="container">The FOMO Experience</h2>\n<p class="container">\n  <br />\n  We started FOMO way back in 1952. Times have changed. Tastes in Music have changed. But here at FOMO our passion of aiding musicians of all ages has not changed.\n  We are determined to help every customer find their sound.  Whether that sound be jazz, rock or classical; guitar, trumpet or didgeridoo. We understand\n  the power of music, and we want to bring that power into the homes of Utah County. FOMO is a store that aims to satisfy the musical needs of musicians and budding\n  musicians in the area. We provide instruments, accessories, repairs, sheet music, and training opportunities. Our friendly staff is waiting to help you find the instrument\n  perfect for you. We have the widest variety of instruments in the state and we are positive that we can find the perfect instrument for you and your family. We believe music\n  can change the world, because music changes people.  We invite you to come change the world with us.\n  <!-- Music can change the world because it can change peopele - Bono -->\n</p>\n\n')
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
{"filename": "C:/Apache24/htdocs/FOMO/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 5, "55": 24, "60": 28, "65": 44, "70": 48, "76": 3, "82": 3, "88": 7, "95": 7, "96": 11, "97": 11, "103": 26, "109": 26, "115": 30, "121": 30, "127": 46, "133": 46, "139": 133}}
__M_END_METADATA
"""
