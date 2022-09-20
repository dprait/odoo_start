# -*- coding: utf-8 -*-
# from odoo import http


# class CheckId(http.Controller):
#     @http.route('/check_id/check_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_id/check_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_id.listing', {
#             'root': '/check_id/check_id',
#             'objects': http.request.env['check_id.check_id'].search([]),
#         })

#     @http.route('/check_id/check_id/objects/<model("check_id.check_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_id.object', {
#             'object': obj
#         })
