from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Description'

    partner_id = fields.Many2one(
        string='Tên khách hàng',
        comodel_name='res.partner'
    )

    loyalty_points = fields.Float(
        string='Tổng số điểm trong 1 đơn hàng'
    )

    money_spent = fields.Float(
        string='Tồng tiền 1 đơn hàng'
    )

    loyalty_point = fields.Float(
        string='Số điểm tích lũy'
    )

    date_order = fields.Datetime(
        string='Thời gian xác nhận đơn hàng'
    )

    name = fields.Char(
        string='Mã đơn hàng'
    )

    @api.model
    def create(self, vals):
        self.btn_send_email()
        return super(LoyaltyHistory, self).create(vals)

    def btn_send_email(self):
        template_obj = self.env['mail.template'].sudo().search([('name', '=', 'Email Template Name')], limit=1)
        if template_obj:
            # receipt_list = ['abc@gmail.com', 'xyz@yahoo.com']
            # email_cc = ['test@gmail.com']

            body = template_obj.body_html
            body = body.replace('--department--', str(self.partner_id.name))
            body = body.replace('--variable_holds_dynamic_data_1--', str(self.loyalty_points))
            # body = body.replace('--variable_holds_dynamic_data_2--', self.field_2)
            # body = body.replace('--variable_holds_dynamic_data_3--', self.field_3)
            # body = body.replace('--variable_holds_dynamic_data_4--', self.field_4)
            # body = body.replace('--product_number_goes_here--', self.product_no)
            # body = body.replace('--brach--', self.branch.name)

            mail_values = {
                'subject': template_obj.subject,
                'body_html': body,
                'email_to': template_obj.email_to,
                # 'email_cc': ';'.join(map(lambda x: x, email_cc)),
                'email_from': template_obj.email_from,
            }
            create_and_send_email = self.env['mail.mail'].create(mail_values).send()
            print(create_and_send_email)
            print('send mail')
            print(self.partner_id)
            print(self.loyalty_points)

