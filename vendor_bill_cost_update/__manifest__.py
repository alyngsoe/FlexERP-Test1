# -*- coding: utf-8 -*-

# Part of Alex Lyngse. See LICENSE file for full copyright and licensing details.


{
    'name': " Vendor Bill Cost Update",
    'version': '1.0',
    'category': 'Accounting',
    'license': 'Other proprietary',
    'summary': """This Module Cost of a product to be updated with the product price on the vendor bill validation,
                 But only if the costing method on the product category is set to standard price.
               """,
    'description': """
       Update the cost of a product from a Vendor bill.
    """,
    'author': 'Alex Lyngse',

    'depends': [
                'account','stock_account'
               ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}
