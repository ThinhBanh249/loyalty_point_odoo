from odoo import fields, models, api


class PartnerLevel(models.Model):
    _name = 'loyalty.program.partner.level'
    _description = 'Description'

    name = fields.Char(
        string='Tên cấp độ',
        required=True
    )

    loyalty_points = fields.Float(
        string='Required point',
        required=True
    )

    description = fields.Text(
        string='Mô tả cấp độ'
    )
