# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520969476.529216
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/about.html'
_template_uri = 'about.html'
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
        def top():
            return render_top(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def maintain():
            return render_maintain(context._locals(__M_locals))
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
        __M_writer('\n  <h1 class="top">About FOMO</h1>\n')
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
        __M_writer('\nThe Family Oriented Music Organization (FOMO) is the oldest established family music store in Utah. Founded in 1936, our commitment to music education and quality products has made us one of the finest music retail stores in the country. <br><br>\n\nWe support school music programs throughout the valley and want to help you any way we can. At Summerhays Music, we understand that your success is our success. Therefore, we make extraordinary efforts to be sure that the instrument you receive is properly set up, of high quality, and will meet the requirements to provide an enjoyable musical experience. We understand that you are making an investment. Likewise, we want to be sure we are making a reciprocal investment in you, our valued customer.<br><br>\n\nMusic is fun and exciting. Choosing the right instrument for that experience is very important. With one of the largest selections of instruments available anywhere, we will find the one that is just right for you. Please feel free to contact our store with any concerns you might have and we’ll be more than happy to assist with your music needs.\n<br /><br />\nWe believe that music should be accessible to all. For that reason we have made sure our website is easily navigated.\nWe have ensured that all fonts are clear and readable and links stand out.  The whole site is easily navigable from the keyboard.\nThe site has also been developed to be easily used by e-readers. We use hiereachical headings and have a go to content link on every page.\nAll the colors on the site have been tested and pass AAA tests for readability.\n')
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
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 5, "54": 9, "59": 13, "64": 26, "69": 30, "75": 3, "81": 3, "87": 7, "93": 7, "99": 11, "105": 11, "111": 15, "117": 15, "123": 28, "129": 28, "135": 129}}
__M_END_METADATA
"""
