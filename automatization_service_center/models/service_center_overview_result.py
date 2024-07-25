from odoo import models, fields, api


class ServiceCenterOverviewResult(models.Model):
    _name = 'service.center.overview.result'
    _description = 'Result of overview'
    """ This model is required to generate a machine inspection report
               """

    lead_id = fields.Many2one(
        comodel_name='service.center.lead',
        required=True,
    )

    service_ids = fields.Many2many(
        comodel_name='service.center.service',
        relation='service_in_overview',
        column1='service_id',
        column2='lead_id',
        required=True,
    )

    comment = fields.Text(

    )

    @api.depends('lead_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.lead_id.display_name}"
            )

    @api.constrains('lead_id')
    def assign_overview_result_for_lead(self):
        for rec in self:
            lead = self.env['service.center.lead'].browse(rec.lead_id.id)
            lead.overview_result_id = rec.id
