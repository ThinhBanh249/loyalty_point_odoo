# -*- coding: utf-8 -*-
# from odoo import http


# class LoyaltyProgram(http.Controller):
#     @http.route('/loyalty_program/loyalty_program', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyalty_program/loyalty_program/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyalty_program.listing', {
#             'root': '/loyalty_program/loyalty_program',
#             'objects': http.request.env['loyalty_program.loyalty_program'].search([]),
#         })

#     @http.route('/loyalty_program/loyalty_program/objects/<model("loyalty_program.loyalty_program"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyalty_program.object', {
#             'object': obj
#         })
