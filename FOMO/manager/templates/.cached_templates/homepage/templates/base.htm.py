# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523549151.520302
_enable_loop = True
_template_filename = 'C:/Apache24/htdocs/FOMO/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['maintain', 'menu', 'top', 'content', 'left', 'center', 'right']


from catalog import models as cmod

import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def maintain():
            return render_maintain(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        def right():
            return render_right(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n')
        __M_writer('\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>FOMO</title>\n\n')
        __M_writer('        <script src="//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n        <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\n        <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/css/bootstrap-theme.min.css" />\n        <link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css" />\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n        <link rel="icon" type="image/x-icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/musicNote.png" />\n    </head>\n    <body>\n      <div class="content">\n\n\n      <a id="skip_to_content" href="#mid">Skip to Main Content</a>\n      <maintenance>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintain'):
            context['self'].maintain(**pageargs)
        

        __M_writer('\n      </maintenance>\n        <header>\n          <nav class="navbar navbar-default navbar-inverse">\n            <div class="container-fluid">\n              <div class="navbar-header">\n                <a class="navbar-brand" id="navimg" href="/homepage/index"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/greyNote.png" alt="Music Note" height="35" width="35"></a>\n              </div>\n              <ul class="nav navbar-nav">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n              </ul>\n              <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated:
            __M_writer('\n')
            if cmod.Order.objects.filter(user=request.user,status="cart").first() is not None:
                if cmod.Order.objects.filter(user=request.user,status="cart").first().num_items() > 0:
                    __M_writer('                        <li>\n                          <a id="home" href="/catalog/cart">\n\n                            ')
                    __M_writer(str(cmod.Order.objects.filter(user=request.user,status="cart").first().num_items()))
                    __M_writer('\n                            <span class=" gly glyphicon glyphicon-shopping-cart"></span>\n                          </a>\n                        </li>\n')
            __M_writer('\n                  <li class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">')
            __M_writer(str(request.user.email))
            __M_writer('\n                    <span class="caret"></span></a>\n                    <ul class="dropdown-menu">\n')
            if request.user.has_perm('auth.manager_view'):
                __M_writer('\t\t\t\t\t\t\t<li><a href="/manager/ProductList">Manager Portal</a></li>\n')
            __M_writer('                      <li><a href="/account/user_orders">Your Orders</a></li>\n                      <li><a href="/account/logout/">Logout</a></li>\n\t\t\t\t\t\t\n                    </ul>\n                  </li>\n')
        else:
            __M_writer('                    <li><a href="/account/signup"><span class="glyphicon glyphicon-user"></span>Register</a></li>\n                    <li><a href="/account/login/"><span class="glyphicon glyphicon-user"></span>Login</a></li>\n\n')
        __M_writer('\n              </ul>\n            </div>\n          </nav>\n\n        </header>\n        <div class="row">\n        <top class="col-md-12">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        __M_writer('\n        </top>\n      </div>\n        <div class="row">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n      </div>\n      </div>\n      <br />\n      <br />\n      <br />\n      <br />\n        <footer class="footer foot col-md-12">\n         <a href="/homepage/index">Home</a> |\n          <a href="/catalog/index">Catalog</a> |\n          <a href="/homepage/about">About</a> |\n          <a href="/homepage/contact">Contact Us</a> |\n          <a href="/homepage/terms">Terms and Conditions</a> |\n          <a href="/homepage/faq">FAQ</a>\n          <br /><br />\n\n            ')
        __M_writer('\n            FOMO - ')
        __M_writer(str( datetime.datetime.now().year ))
        __M_writer(' &copy\n\n        </footer>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintain(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintain():
            return render_maintain(context)
        __M_writer = context.writer()
        __M_writer('\n          <!-- maintenance messages go here in sub-templates. -->\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\n                <!-- <li><a href="#">Custom nav bar will go here</a></li> -->\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        __M_writer('\n          <!-- top info goes here -->\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def left():
            return render_left(context)
        def right():
            return render_right(context)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n        <div class = "lefty col-md-2">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n        </div>\n        <div id="mid" class = "middy col-md-8">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n        </div>\n        <div class = "righty  col-md-2">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right'):
            context['self'].right(**pageargs)
        

        __M_writer('\n        </div>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n          <!-- left col -->\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n          <!-- center col -->\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right():
            return render_right(context)
        __M_writer = context.writer()
        __M_writer('\n          <!-- right col -->\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Apache24/htdocs/FOMO/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 3, "20": 120, "22": 0, "44": 2, "45": 3, "46": 11, "47": 12, "48": 12, "49": 13, "50": 13, "51": 14, "52": 14, "53": 17, "54": 18, "55": 18, "56": 19, "57": 19, "62": 29, "63": 35, "64": 35, "69": 40, "70": 43, "71": 44, "72": 45, "73": 46, "74": 47, "75": 50, "76": 50, "77": 56, "78": 58, "79": 58, "80": 61, "81": 62, "82": 64, "83": 69, "84": 70, "85": 74, "90": 84, "95": 104, "96": 120, "97": 121, "98": 121, "104": 27, "110": 27, "116": 38, "122": 38, "128": 82, "134": 82, "140": 88, "152": 88, "157": 92, "162": 97, "167": 102, "173": 90, "179": 90, "185": 95, "191": 95, "197": 100, "203": 100, "209": 203}}
__M_END_METADATA
"""
