# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523483598.2528012
_enable_loop = True
_template_filename = 'C:/Apache24/htdocs/FOMO/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
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
    ns = runtime.ModuleNamespace('fl', context._clean_inheritance_tokens(), callables=None, calling_uri=_template_uri, module='formlib.tags')
    context.namespaces[(__name__, 'fl')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def center():
            return render_center(context._locals(__M_locals))
        total = context.get('total', UNDEFINED)
        fl = _mako_get_namespace(context, 'fl')
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n')
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
        __M_writer = context.writer()
        __M_writer('\n  <h1 class="push-center">Checkout</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        fl = _mako_get_namespace(context, 'fl')
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<br />\n\n<h2>Your Total: ')
        __M_writer(str(total))
        __M_writer('</h2>\n')
        __M_writer('\n')
        def ccall(caller):
            def body():
                int = context.get('int', UNDEFINED)
                settings = context.get('settings', UNDEFINED)
                cart = context.get('cart', UNDEFINED)
                __M_writer = context.writer()
                __M_writer('\n  <div class="text-center">\n    <script\n        src="https://checkout.stripe.com/checkout.js"\n        class="stripe-button"\n        data-key="')
                __M_writer(str(settings.STRIPE_PUBLIC_KEY))
                __M_writer('"\n        data-amount="')
                __M_writer(str(int(cart.total_price * 100)))
                __M_writer('"\n        data-description="Thank you for choosing FOMO"\n        data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\n        data-local="auto"\n        data-label="Pay Now">\n    </script>\n\n  </div>\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(str(fl.render()))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Apache24/htdocs/FOMO/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"25": 9, "31": 0, "42": 1, "47": 4, "52": 25, "58": 2, "64": 2, "70": 5, "78": 5, "79": 8, "80": 8, "81": 9, "88": 10, "89": 15, "90": 15, "91": 16, "92": 16, "97": 10, "100": 24, "106": 100}}
__M_END_METADATA
"""
