# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517351002.8412778
_enable_loop = True
_template_filename = '/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        def maintain():
            return render_maintain(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
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
        __M_writer('\n<h1 class="title">Terms and Conditions</h1>\n')
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
        __M_writer('\n<div class="terms">\n<p>\n  Last updated: January 18, 2018\n</p>\n\n  <p>Please read these Terms and Conditions carefully before using\n  the http://www.FOMO.com website and the My Mobile App mobile\n  application (the "Service") operated by My Company.\n  Your access to and use of the Service is conditioned on your acceptance of and compliance with\n  these Terms. These Terms apply to all visitors, users and others who access or use the Service.\n  By accessing or using the Service you agree to be bound by these Terms. If you disagree\n  with any part of the terms then you may not access the Service.\n  <h4>Purchases</h4>\n  If you wish to purchase any product or service made available through the Service,\n  you may be asked to supply certain information relevant to your Purchase including, without\n  limitation, your …\n  The Purchases section is for businesses that sell online (physical or digital). For the full\n  disclosure section, create your own Terms and Conditions.\n  Subscriptions\n  Some parts of the Service are billed on a subscription basis ("Subscription(s)"). You will be billed in\n  advance on a recurring ...\n  The Subscriptions section is for SaaS businesses. For the full disclosure section, create your\n  own Terms and Conditions.\n  <h4>Content</h4>\n  Our Service allows you to post, link, store, share and otherwise make available certain information,\n  text, graphics, videos, or other material. You are responsible for the …\n  The Content section is for businesses that allow users to create, edit, share, make content on\n  their websites or apps. For the full disclosure section, create your own Terms and Conditions.\n  Links To Other Web Sites\n  Our Service may contain links to third\xadparty web sites or services that are not owned or controlled\n  by FOMO.\n  FOMO has no control over, and assumes no responsibility for, the content,\n  privacy policies, or practices of any third party web sites or services. You further acknowledge and\n  agree that My Company (change this) shall not be responsible or liable, directly or indirectly, for any\n  damage or loss caused or alleged to be caused by or in connection with use of or reliance on any\n  such content, goods or services available on or through any such web sites or services.\n  <h4>Changes</h4>\n  We reserve the right, at our sole discretion, to modify or replace these Terms at any time. If a\n  revision is material we will try to provide at least 30 (change this) days\' notice prior to any new terms\n  taking effect. What constitutes a material change will be determined at our sole discretion.\n  <h4>Contact Us</h4>\n  If you have any questions about these Terms, please contact us.\n</p>\n')
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
{"filename": "/Users/danejensen/is414/FomoProject/FOMO/homepage/templates/terms.html", "uri": "terms.html", "source_encoding": "utf-8", "line_map": {"28": 0, "43": 1, "48": 5, "53": 9, "58": 13, "63": 59, "68": 63, "74": 3, "80": 3, "86": 7, "92": 7, "98": 11, "104": 11, "110": 15, "116": 15, "122": 61, "128": 61, "134": 128}}
__M_END_METADATA
"""
