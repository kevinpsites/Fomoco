# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523478830.8752131
_enable_loop = True
_template_filename = 'C:/Apache24/htdocs/FOMO/catalog/templates/email_receipt.html'
_template_uri = 'email_receipt.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tax = context.get('tax', UNDEFINED)
        order = context.get('order', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="UTF-8">\n    <title>title</title>\n    <style>\n        .receipt {\n            font-family: arial, sans-serif;\n            border-collapse: collapse;\n            width: 100%;\n        }\n\n        .receipt td, th {\n            border: 1px solid #dddddd;\n            text-align: left;\n            padding: 8px;\n        }\n\n        .receipt tr:nth-child(even) {\n            background-color: #dddddd;\n        }\n</style>\n  </head>\n  <body>\n    <p style="font-size:400%; font-family:serif;  margin:0 0 0 1em; border-bottom:solid #aaaaaa ">\n      FOMO\n    </p>\n    <h1 style="text-align:right; padding-right:1em;">Order Confirmation</h1>\n  <div style=" border-top:solid black; padding:0px 3% ">\n\n    <div style="width:48%;  float:left;">\n      <H1>Purchase Summary</H1>\n\t\t<h2>Order Date: ')
        __M_writer(str(order.order_date.month))
        __M_writer('/')
        __M_writer(str(order.order_date.day))
        __M_writer('/')
        __M_writer(str(order.order_date.year))
        __M_writer('\n      <h3 style="margin-bottom:2px;">Your order is on its way to:</h3>\n      <p style="font-size:120%; margin-top:2px;">')
        __M_writer(str(order.ship_address))
        __M_writer(', ')
        __M_writer(str(order.ship_city))
        __M_writer(', ')
        __M_writer(str(order.ship_state))
        __M_writer(' ')
        __M_writer(str(order.ship_zip_code))
        __M_writer('</p>\n    </div>\n    <div style="float:left; margin:10% 0 0 15%;">\n      <table style="border-spacing:0 12px 0 12px;align-content:right; margin-left:3%">\n        <tr >\n          <td style="font-size:150%">Subtotal:</td>\n\n\n          <td style="margin-left:10%;font-size:150%">')
        __M_writer(str('${:,.2f}'.format(order.total_price - tax.price)))
        __M_writer('</td>\n        </tr>\n        <tr >\n          <td style="font-size:150%">Tax:</td>\n\n\n          <td style="margin-left:10%;font-size:150%">')
        __M_writer(str('${:,.2f}'.format(tax.price)))
        __M_writer('</td>\n        </tr>\n        <tr style="border-top:black solid;">\n          <td style="font-size:150% ">Total:</td>\n\n\n          <td style="margin-left:10%;font-size:150%">')
        __M_writer(str('${:,.2f}'.format(order.total_price)))
        __M_writer('</td>\n        </tr>\n      </table>\n\n    </div>\n  </div>\n  <br />\n  <br />\n  <br />\n\n<h3 style="clear:both; padding-top:20px; margin-bottom:2px;">Order Details | Order #')
        __M_writer(str(order.id))
        __M_writer('</h3>\n  <table class="receipt"style="width:100%; ">\n  <tr>\n    <th>Product</th>\n    <th>Price</th>\n    <th>Qty</th>\n    <th>Row Total</th>\n  </tr>\n')
        for i in items:
            __M_writer('  <tr>\n    <td>')
            __M_writer(str(i.product.name))
            __M_writer('</td>\n    <td>')
            __M_writer(str('${:,.2f}'.format(i.price)))
            __M_writer('</td>\n    <td>')
            __M_writer(str(i.quantity))
            __M_writer('</td>\n    <td>')
            __M_writer(str('${:,.2f}'.format(i.extended)))
            __M_writer('</td>\n  </tr>\n')
        __M_writer('\n</table>\n<br />\n\n\n<p style="text-align:center; font-size:200%">\n  <strong>Thank you for shopping with us! </strong><br />\n  <a href="https://www.fomoco.me" style="text-decoration:none; font-size:75%">Visit us again soon</a>\n  \n</p>\n<p style="text-align:center; font-size:100%;">\nPlease do not reply to this message\n</p>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Apache24/htdocs/FOMO/catalog/templates/email_receipt.html", "uri": "email_receipt.html", "source_encoding": "utf-8", "line_map": {"18": 0, "26": 1, "27": 33, "28": 33, "29": 33, "30": 33, "31": 33, "32": 33, "33": 35, "34": 35, "35": 35, "36": 35, "37": 35, "38": 35, "39": 35, "40": 35, "41": 43, "42": 43, "43": 49, "44": 49, "45": 55, "46": 55, "47": 65, "48": 65, "49": 73, "50": 74, "51": 75, "52": 75, "53": 76, "54": 76, "55": 77, "56": 77, "57": 78, "58": 78, "59": 81, "65": 59}}
__M_END_METADATA
"""
