from odoo import models, fields, api


class ServiceCenterLead(models.Model):
    _name = 'service.center.lead'
    _description = 'Lead with all information'
    """ This information is needed to process leads and review their status
               """

    status = fields.Selection(
        [
            ('entry', 'Entry'),
            ('reviewed', 'Reviewed'),
            ('repairing', 'Repairing'),
            ('repaired', 'Repaired'),
        ],
        default='entry',
    )

    car_id = fields.Many2one(
        comodel_name='service.center.car'
    )

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        related='car_id.res_partner_id'
    )

    overview_slot_id = fields.Many2one(
        comodel_name='service.center.slot',
        domain=[('is_booked', '=', False)],
    )

    engineer_id = fields.Many2one(
        comodel_name='res.users',
        related='overview_slot_id.engineer_id',
    )

    overview_result_id = fields.Many2one(
        comodel_name='service.center.overview.result'
    )

    comment = fields.Text(

    )

    @api.depends('car_id', 'res_partner_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.res_partner_id.display_name}-"
                f"{rec.car_id.display_name}"
            )

    @api.constrains('overview_slot_id')
    def _book_the_slot(self):
        for rec in self:
            slot = self.env['service.center.slot'].browse(
                rec.overview_slot_id.id
            )
            slot.is_booked = True
