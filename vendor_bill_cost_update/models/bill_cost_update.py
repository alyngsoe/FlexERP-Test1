# -*- coding: utf-8 -*-

from odoo import api, models, fields 

class AccountInvoice(models.Model):

	_inherit = 'account.invoice'


	@api.multi
	def invoice_validate(self):
		res = super(AccountInvoice, self).invoice_validate()
		for invoice in self:
			if invoice.type == 'in_invoice':
				for line in invoice.invoice_line_ids:
					if line.product_id.categ_id.property_cost_method == 'standard':
						price_unit = line.price_unit
						if invoice.currency_id != invoice.company_id.currency_id:
							price_unit = invoice.currency_id.compute(line.price_unit, invoice.company_id.currency_id)
						line.product_id.write({'standard_price': price_unit})
		return res
