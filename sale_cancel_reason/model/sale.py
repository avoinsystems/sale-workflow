# Copyright 2013 Guewen Baconnier, Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cancel_reason_id = fields.Many2one(
        'sale.order.cancel.reason',
        string="Reason for cancellation",
        readonly=True,
        ondelete="restrict")

    @api.multi
    def wizard_sale_order_cancel(self):
        self.ensure_one()
        action = self.env.ref('sale_cancel_reason.action_sale_order_cancel').read()[0]
        return action


class SaleOrderCancelReason(models.Model):
    _name = 'sale.order.cancel.reason'
    _description = 'Sale Order Cancel Reason'

    name = fields.Char('Reason', required=True, translate=True)
