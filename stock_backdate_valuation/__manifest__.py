# -*- coding: utf-8 -*-
{
    'name' : 'Stock Back Date Valuation',
    'version' : '1.0',
    'price' : 0.0,
    'currency': 'EUR',
    'category': 'Hidden',
    'license': 'Other proprietary',
    'author': 'Alex Lyngsøe',
    'website': 'www.odoo.com',
    'description': """

Menu Path: Inventory/Reporting/Inventory.
For Delivery Validating / Incoming receipts:
We can open Date of transfer / Date done on stock.picking and store this Date done on Stock.move with new field called "Back Date". So "Back Date" on stock move will be compute from Date done of picking/transfer.. And at end we may need to adapt this report Inventory/Reporting/Inventory which should consider backdate on stock move.
Currently date is taken from stock move - 
Schedule date and report is generated based on that
If we can create new field on stock move which is computed using 
date of transfer of related picking and use this new date field instead of stock move - schedule date then it can fix issue.

            """,
    'summary' : 'Stock Back Date Valuation',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'depends' : ['stock_account'],
    'data' : [
#               'security/ir.model.access.csv',
#               'security/stock_account_security.xml',
            'views/stock_move_view.xml',
#               'views/stock_valuation_history_view.xml',
#               'wizard/update_Inventory_wizard_view.xml',
              ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
