# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'Multiple Branch/Unit Setup for Company (Community)',
    'category': 'General',
    'summary': 'This module allows to use for multi-branch concept for single or multi company',
    'description': """This module allows to use for multi-branch concept for single or multi company""",
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'website': 'http://www.acespritech.com',
    'price': 49.00,
    'currency': 'EUR',
    'version': '1.0.1',
    'depends': ['base', 'sale_management', 'stock', 'purchase', 'account', 'sale_stock'],
    'images': ['static/description/main_screenshot.png'],
    'data': [
             'security/branch_security.xml',
             'security/ir.model.access.csv',
             'views/branch_view.xml',
             'views/res_partner_view.xml',
             'views/stock_view.xml',
             'views/sale_view.xml',
             'views/purchase_view.xml',
             'views/account_view.xml',
             'views/res_company_view.xml',
             'report/sale_report_views.xml',
             'report/purchase_report_views.xml',
             'report/account_invoice_report_view.xml',
             'wizard/account_report_common_view.xml',
             'report/sale_report_templates.xml',
        ],
    'installable': True,
    'auto_install': False,
    'post_init_hook':'post_init_check'

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
