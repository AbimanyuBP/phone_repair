# -*- coding: utf-8 -*-
# from odoo import http


# class PhoneRepair(http.Controller):
#     @http.route('/phone_repair/phone_repair/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phone_repair/phone_repair/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phone_repair.listing', {
#             'root': '/phone_repair/phone_repair',
#             'objects': http.request.env['phone_repair.phone_repair'].search([]),
#         })

#     @http.route('/phone_repair/phone_repair/objects/<model("phone_repair.phone_repair"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phone_repair.object', {
#             'object': obj
#         })
