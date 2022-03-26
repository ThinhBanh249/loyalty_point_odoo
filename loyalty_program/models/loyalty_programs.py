from odoo import fields, models, api


class LoyaltyProgram(models.Model):
    _name = 'loyalty.program'
    _description = 'Loyalty program'

    name = fields.Char(
        string='Tên chương trình khuyến mãi',
        required=True
    )

    points = fields.Float(
        string='Số % point trên 1 đơn hàng',
        required=True
    )

    active = fields.Boolean(
        string='Trạng thái chương trình khuyến mãi',
        required=True,
        default=True
    )
