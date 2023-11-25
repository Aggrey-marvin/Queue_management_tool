from odoo import fields, api, models, _


class CounterCreate(models.Model):
    _name = 'counter.counter'

    name = fields.Char(string="COUNTER", required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    counter_name = fields.Char(string="Counter Name")
    department_name = fields.Many2one('hr.department', string="Department")
    employee_id = fields.Many2one("hr.employee", string="Employee")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('counter.sequence') or _('New')
        result = super(CounterCreate, self).create(vals)
        return result
