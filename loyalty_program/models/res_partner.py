from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_point = fields.Float(
        string='Số điểm tích lũy',
        default=0
    )

    loyalty_level = fields.Many2one(
        comodel_name='loyalty.program.partner.level',
        string='Cấp độ khách hàng',
        compute='loyalty_level_compute'
    )

    @api.depends('loyalty_point')
    def loyalty_level_compute(self):
        for rec in self:
            print(rec.loyalty_level)
            if rec.loyalty_point:
                levels = self.env['loyalty.program.partner.level'].sudo().search([])
                print(levels)
                x = 0
                for level in levels:
                    if (level.loyalty_points >= x) and (rec.loyalty_point > level.loyalty_points):
                        rec.loyalty_level = level
                        print(level)
                        print(rec.loyalty_level)
                        x = level.loyalty_points
