from odoo import api, fields, models

class TokenTokenInherit(models.Model):
    _inherit =  "token.token"

    counter_id = fields.Many2one("counter.counter", string="Counter", 
                                 compute="_compute_counter_id")
    state = fields.Selection(selection=[('new', 'New'),
                                        ('service', 'Service'),
                                        ('done', 'Done')],
                                        default='new', string="Token Status")
    

    @api.depends('department')
    def _compute_counter_id(self):
        for record in self:
            counters = record.department.counter_ids
            sorted_counters = sorted(counters, key=lambda r: r.tokens)
            if sorted_counters:
                record.counter_id = sorted_counters[0].id
            else:
                record.counter_id = None
            