from odoo import models, fields


class SaleReport(models.Model):

    _inherit = 'sale.report'

    cancel_reason_id = fields.Many2one(
        comodel_name="sale.order.cancel.reason",
        string="Reason for cancellation",
        readonly=True
    )

    # pylint: disable=dangerous-default-value
    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields.update({
            'cancel_reason_id': ', s.cancel_reason_id as cancel_reason_id'
        })
        groupby += ", s.cancel_reason_id"

        return super()._query(with_clause, fields, groupby, from_clause)
