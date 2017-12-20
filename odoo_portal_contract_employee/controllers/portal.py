# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from odoo.exceptions import AccessError
from odoo.addons.portal.controllers.portal import get_records_pager, CustomerPortal, pager as portal_pager

#class website_account(website_account):
class CustomerPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        employee = request.env['hr.employee'].sudo().search([('user_id', '=', request.env.user.id)])
        values.update({
            'contract_count': request.env['hr.contract'].sudo().search_count([('employee_id', '=', employee.id)]),
        })
        return values
        
    @http.route(['/my/contracts', '/my/contracts/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_contracts(self, page=1, **kw):
        if request.env['res.users'].browse(request.session.uid).user_has_groups('odoo_portal_contract_employee.group_employee_contract'):
            values = self._prepare_portal_layout_values()
            employee = request.env['hr.employee'].sudo().search([('user_id', '=', request.env.user.id)])
            if employee:
                    contract = request.env['hr.contract'].sudo().search([('employee_id', '=', employee.id)])
                    contract_count = len(contract)
                    # count for pager
                    # pager
                    pager = request.website.pager(
                        url="/my/contracts",
                        total=contract_count,
                        page=page,
                        step=self._items_per_page
                    )
                    values.update({
                        'contracts': contract,
                        'page_name': 'contract',
                        'pager': pager,
                        'default_url': '/my/contracts',
                    })
                    return request.render("odoo_portal_contract_employee.portal_my_contracts", values)
                
    @http.route(['/my/contract/<int:contract>'], type='http', auth="user", website=True)
    def contract_print(self, contract, access_token=None, **kw):
        if request.env['res.users'].browse(request.session.uid).user_has_groups('odoo_portal_contract_employee.group_employee_contract'):
            # print report as sudo, since it require access to taxes, payment term, ... and portal
            # does not have those access rights.
            pdf = request.env.ref('print_employee_contract.employee_contract_report_print').sudo().render_qweb_pdf([contract])[0]
            pdfhttpheaders = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf)),
            ]
            return request.make_response(pdf, headers=pdfhttpheaders)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
