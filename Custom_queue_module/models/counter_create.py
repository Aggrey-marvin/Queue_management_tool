from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class CounterCreateInherit(models.Model):
    _inherit = "counter.counter"

    employee_id = fields.Many2one("hr.employee", string="Employee")


    @api.onchange('department_name')
    def _onchange_department_name(self):
        employee_ids = self.department_name.member_ids.mapped('id')
        return {'domain':{'employee_id':[('id','in',employee_ids)]}}
    