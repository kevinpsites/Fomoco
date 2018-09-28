# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523546904.850462
_enable_loop = True
_template_filename = 'C:/Apache24/htdocs/FOMO/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['left', 'right']


from catalog import models as cmod

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
    return runtime._inherit_from(context, '/homepage/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        def right():
            return render_right(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        name = context.get('name', UNDEFINED)
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<br />\n<br />\n<ul id="catalog" class="nav  nav-pills nav-stacked">\n  <li>\n    <a href="/catalog/index/" type="button" id="butt"class="but btn btn-primary nav-item category_nav ')
        __M_writer(str('on' if name == 'All Products' else 'off'))
        __M_writer('">All Products</a>\n  </li>\n')
        for item in cmod.Category.objects.order_by('name'):
            __M_writer('  <li>\n\n    <a href="/catalog/index/')
            __M_writer(str(item.id))
            __M_writer('" type="button" id="butt"class="but btn btn-primary nav-item category_nav ')
            __M_writer(str('on' if item.name == name else 'off'))
            __M_writer('">')
            __M_writer(str(item.name))
            __M_writer('</a>\n  </li>\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        request = context.get('request', UNDEFINED)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<p class="titl">\n  Recently Viewed:\n</p>\n  <ol id="proList">\n    ')
        i = 0  
        
        __M_writer('\n')
        for item in request.last_five:
            if product != item and i != 5:
                __M_writer('    <li>\n      <a href="/catalog/details/')
                __M_writer(str(item.id))
                __M_writer('">\n        <div class="dib">\n          <img class="lil_prod" src=')
                __M_writer(str(item.image_url()))
                __M_writer(' alt="" >\n          <h2 class=\'lname\'>')
                __M_writer(str(item.name))
                __M_writer('</h2>\n        </div>\n\n      </a>\n    </li>\n    ')
                i = i + 1 
                
                __M_writer('\n')
        __M_writer('  </ol>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Apache24/htdocs/FOMO/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "43": 1, "44": 2, "49": 19, "54": 43, "60": 5, "67": 5, "68": 10, "69": 10, "70": 12, "71": 13, "72": 15, "73": 15, "74": 15, "75": 15, "76": 15, "77": 15, "78": 18, "84": 21, "92": 21, "93": 27, "95": 27, "96": 28, "97": 29, "98": 30, "99": 31, "100": 31, "101": 33, "102": 33, "103": 34, "104": 34, "105": 39, "107": 39, "108": 42, "114": 108}}
__M_END_METADATA
"""
