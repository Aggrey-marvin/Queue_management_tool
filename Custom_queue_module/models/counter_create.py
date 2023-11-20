from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class CounterCreateInherit(models.Model):
    _inherit = "counter.counter"

    employee_id = fields.Many2one("hr.employee", string="Employee")
    token_ids = fields.One2many("token.token", "counter_id", string="Counter Tokens")
    tokens = fields.Integer(string="Clients", compute="_compute_tokens")


    @api.onchange('department_name')
    def _onchange_department_name(self):
        employee_ids = self.department_name.member_ids.mapped('id')
        return {'domain':{'employee_id':[('id','in',employee_ids)]}}
    

    @api.depends('token_ids')
    def _compute_tokens(self):
        for record in self:
            record.tokens = len(record.token_ids)