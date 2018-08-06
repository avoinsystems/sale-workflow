# See LICENSE for licensing information

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class SaleReport(models.Model):

    _inherit = 'sale.report'

    cancel_reason = fields.Char(
        string="Reason for cancellation",
        readonly=True)

    def _select(self):
        select_str = super(SaleReport, self)._select()
        select_str += ", scr.name as cancel_reason"
        return select_str

    def _from(self):
        from_str = super(SaleReport, self)._from()
        from_str += "left join sale_order_cancel_reason scr on scr.id = s.cancel_reason_id"
        return from_str

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += ", scr.name"
        return group_by_str
