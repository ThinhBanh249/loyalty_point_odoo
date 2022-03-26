# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class loyalty_program(models.Model):
#     _name = 'loyalty_program.loyalty_program'
#     _description = 'loyalty_program.loyalty_program'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
