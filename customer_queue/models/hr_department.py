from odoo import fields, models

class HrDepartmentInherit(models.Model):
    _inherit = "hr.department"

    counter_ids = fields.One2many('counter.counter', 'department_name', string="Counters")