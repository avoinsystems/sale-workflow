# Copyright 2013 Guewen Baconnier, Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Sale Cancel Reason',
    'version': '12.0.1.0.0',
    'author': "Camptocamp,Odoo Community Association (OCA)",
    'category': 'Sale',
    'license': 'AGPL-3',
    'complexity': 'normal',
    'website': "https://github.com/OCA/sale-workflow/tree/12.0/sale_cancel_reason",
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_order_cancel_reason.xml',
        'wizard/cancel_reason_view.xml',
        'view/sale_view.xml',
    ],
    'auto_install': False,
    'installable': True,
}
