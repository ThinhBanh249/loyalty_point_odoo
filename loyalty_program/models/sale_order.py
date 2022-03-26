from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _default_loyalty_program(self):
        loyalty_id = int(self.env['ir.config_parameter'].sudo().get_param('loyalty_for_sale_id', False))
        loyalty = self.env['loyalty.program'].browse(loyalty_id)
        return loyalty if loyalty_id and loyalty.exists() else None

    loyalty_program_id = fields.Many2one(
        comodel_name='loyalty.program',
        string='Chương trình khuyến mãi',
        default=_default_loyalty_program
    )

    point_accum = fields.Float(
        string='Point đạt được',
        compute='count_point',
        store=True,
    )

    @api.depends('amount_total')
    def count_point(self):
        for rec in self:
            if rec.amount_total and rec.loyalty_program_id:
                bill = float(rec.amount_total)
                rec.point_accum = bill * rec.loyalty_program_id.points / 100
                # print(str(rec.tax_totals_json))
                print('ád')
                print(rec.amount_total)



    def action_confirm(self):
        result = super(SaleOrder, self).action_confirm()
        if self.state == 'sale':
            vals={
                'partner_id': self.partner_id.ids[0],
                'loyalty_points': self.point_accum,
                'money_spent': float(self.amount_total),
                'date_order': self.date_order,
                'name': self.name

            }
            self.env['loyalty.history'].create(vals)
            self.env['res.partner'].sudo().search([('id','=',self.partner_id.ids[0])]).write({
                'loyalty_point': self.partner_id.loyalty_point + self.point_accum
            })
            print(self.partner_id.loyalty_point + self.point_accum)
        return result