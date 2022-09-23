# -*- coding: utf-8 -*-
# from odoo import http


# class Add-id(http.Controller):
#     @http.route('/add-id/add-id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add-id/add-id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add-id.listing', {
#             'root': '/add-id/add-id',
#             'objects': http.request.env['add-id.add-id'].search([]),
#         })

#     @http.route('/add-id/add-id/objects/<model("add-id.add-id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add-id.object', {
#             'object': obj
#         })
