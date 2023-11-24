from odoo import fields, api, models, _


class TokenCreate(models.Model):
    _name = 'token.token'

    name = fields.Char(string="TOKEN", required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    customer_name = fields.Char(string="Customer Name")
    customer_mobile = fields.Integer(string="Mobile")
    department = fields.Many2one('hr.department', string="Department")
    service_done = fields.Boolean(default=False, string="Service Done?")
    web_created = fields.Boolean(default=False, string="Created on Web")
    counter_id = fields.Many2one("counter.counter", string="Counter", 
                                 compute="_compute_counter_id", store=True)
    state = fields.Selection(selection=[('new', 'New'),
                                        ('waiting', 'Waiting'),
                                        ('service', 'Service'),
                                        ('done', 'Done')],
                                        default='new', string="Token Status")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New') and not vals.get('web_created'):
            vals['name'] = self.env['ir.sequence'].next_by_code('customer.sequence') or _('New')
        result = super(TokenCreate, self).create(vals)
        return result
    

    @api.depends('department')
    def _compute_counter_id(self):
        for record in self:
            counters = record.department.counter_ids
            
            sorted_counters = sorted(counters, key=lambda r: r.tokens)
            if sorted_counters and not record.web_created:
                record.counter_id = sorted_counters[0].id
            elif not record.web_created:
                record.counter_id = None
