# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class add-id(models.Model):
#     _name = 'add-id.add-id'
#     _description = 'add-id.add-id'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
