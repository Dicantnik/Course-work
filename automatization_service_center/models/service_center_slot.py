from odoo import models, fields, api


class ServiceCenterSlot(models.Model):
    _name = 'service.center.slot'
    _description = 'Model for slots of timetable'
    """ This model is needed to store slots when
     an engineer can inspect the customer's machine
               """

    engineer_id = fields.Many2one(
        comodel_name='res.users',
        required=True,
    )

    date = fields.Date(
        required=True,
    )

    hour_from = fields.Float(
        string='Work from',
        required=True,
    )

    hour_to = fields.Float(
        string='Work to',
        required=True
    )

    is_booked = fields.Boolean(

    )

    @api.depends('engineer_id', 'date', 'hour_from', 'hour_to')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.engineer_id.display_name}, "
                f"{rec.date} "
                f"{int(rec.hour_from * 60 // 60)}:"
                f"{int(rec.hour_from * 60 % 60)}-"
                f"{int(rec.hour_to * 60 // 60)}:"
                f"{int(rec.hour_to * 60 % 60)}"
            )
