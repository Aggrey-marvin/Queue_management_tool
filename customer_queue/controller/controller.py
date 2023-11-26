from odoo import http
from odoo.http import request

class CustomerQueue(http.Controller):

    @http.route('/token/generate/', website=True ,auth='public')
    def index(self, **kw):
        context = {}
        departments = request.env['hr.department'].sudo().search([])
        counters = request.env['counter.counter'].sudo().search([])

        context['departments'] = departments

        if request.httprequest.method == 'GET':
            token = request.env['ir.sequence'].sudo().next_by_code('customer.sequence')
            context['token'] = token
            return http.request.render("customer_queue.web_customer_queue", context)
        if request.httprequest.method == "POST":
            selected_couters = [counter for counter in counters if counter.department_name.id == int(kw.get('department'))]
            sorted_counters = sorted(selected_couters, key=lambda r: r.tokens)

            token_name = kw.get('token')

            token_exists = request.env['token.token'].sudo().search([('name', '=', token_name)])

            if not token_exists:
                token = request.env['token.token'].sudo().create({
                    'name': token_name,
                    'customer_name': kw.get('name'),
                    'customer_mobile': kw.get('phone'),
                    'department': kw.get('department'),
                })

                token.sudo().write({'counter_id': sorted_counters[0].id})

                new_context = {
                    'token': token.name,
                    'counter': token.sudo().counter_id.name,
                    'state': token.state,
                }
            else:
                new_context = {
                    'token': token_exists.name,
                    'counter': token_exists.sudo().counter_id.name,
                    'state': token_exists.state,
                }

            return http.request.render("customer_queue.web_token", new_context)



            