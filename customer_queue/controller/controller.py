from odoo import http
from odoo.http import request

class CustomerQueue(http.Controller):

    @http.route('/token/generate/', website=True ,auth='public')
    def index(self, **kw):
        context = {}
        departments = request.env['hr.department'].sudo().search([])
        token = request.env['ir.sequence'].sudo().next_by_code('customer.sequence')

        context['departments'] = departments
        context['token'] = token

        if request.httprequest.method == 'GET':
            return http.request.render("customer_queue.web_customer_queue", context)
        if request.httprequest.method == "POST":
            token = request.env['token.token'].sudo().create({
                'name': kw.get('token'),
                'customer_name': kw.get('name'),
                'customer_mobile': kw.get('phone'),
                'department': kw.get('department')
            })
            print("")
            print("This is the final token: ", token.sudo().name)
            print("")


            