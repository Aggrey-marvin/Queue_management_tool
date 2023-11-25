from odoo import fields, api, SUPERUSER_ID, models, _, Command
from odoo.exceptions import ValidationError


class CustomerService(models.TransientModel):
    _name = 'customer.service'

    user_name = fields.Many2one('res.users', default=lambda self: self.env.user.id)
    date = fields.Datetime(default=fields.Datetime.now, string="Date")
    counter = fields.Many2one('counter.counter', string="Counter", readonly=True)
    customer_service_line_ids = fields.One2many('customer.service.line', 'customer_service_line_id', string="ids")

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)

        counter = self.env['counter.counter'].search([('employee_id', '=', self.env.user.employee_id.id)])

        defaults['counter'] = counter.id
        line_ids = [Command.create({
            'customer': token.name,
            'customer_name': token.customer_name,
            'customer_mobile': token.customer_mobile,
            'service_comment': token.customer_comment
        }) for token in counter.token_ids if token.state != 'done']
        defaults['customer_service_line_ids'] = line_ids

        return defaults

    def customer_service(self):
        token_data = self.env['token.token'].search([('service_done', '=', False)], limit=1)
        print("data", token_data)
        token_list = []
        if token_data:
            for rec in token_data:
                self.customer_service_line_ids += self.env['customer.service.line'].new(
                    {
                        'customer': rec.name,
                        'customer_name': rec.customer_name,
                        'customer_mobile': rec.customer_mobile,
                    }
                )
        else:
            raise ValidationError(_("Not available token"))
        token = self.env['token.show'].search([])
        print("id", type(token), token)
        print("num", token.token_number)
        for test in self.customer_service_line_ids:
            token.token_number = test.customer
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'customer.service',
            'target': 'new',
            'res_id': self.id
        }


class CustomerServiceLine(models.TransientModel):
    _name = 'customer.service.line'

    customer = fields.Char(string="Token")
    customer_name = fields.Char(string="Customer Name")
    customer_mobile = fields.Integer(string="Mobile")
    customer_call = fields.Boolean(default=False, string="Call")
    service_comment = fields.Text(string="Service comment")
    customer_service_line_id = fields.Many2one('customer.service', string="id")
    state = fields.Selection(selection=[('waiting', 'Waiting'),
                                        ('service', 'Service'),
                                        ('done', 'Done')],
                                        default='waiting', string="Token Status")

    def service_given(self):
        token_data = self.env['token.token'].search([('name', '=', self.customer)])
        

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'customer.service',
            'target': 'new',
        }

    @api.onchange('customer_call')
    def onchange_customer_call(self):
        if self.customer_call:
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
                'model': 'token.show'
            }
