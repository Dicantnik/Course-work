from odoo import _, api, models, fields
from odoo.exceptions import ValidationError


class ServiceCenterTimeTable(models.Model):
    _name = 'service.center.time.table'
    _description = 'Model for timetable of engineers'
    """ This model is needed to store and generate
     machine inspection schedules for the engineer
               """

    engineer_id = fields.Many2one(
        comodel_name='res.users',
        required=True,
        domain=[('is_engineer', '=', True)],
    )

    engineer_calendar_ids = fields.One2many(
        comodel_name='service.center.engineer.calendar',
        inverse_name='time_table_id',
    )

    @api.constrains('engineer_calendar_ids', 'engineer_id')
    def confirm_calendar(self):
        """ This method makes slots according
         to the duration of the machine inspection specified in this service
                       """
        duration_of_overview = int(self.env.ref(
            'automatization_service_center.service_center_overview'
        ).duration * 60)
        engineer = self.engineer_id
        if self.env['service.center.time.table'].search_count(
                [('engineer_id', '=', engineer.id)]) > 1:
            raise ValidationError(_('Can`t create 2 timetables'
                                    ' for one engineer'))
        for line in self.engineer_calendar_ids:
            # Here taking every line and make slots with converting
            start_time_slot_min = int(line.hour_from * 60)
            finish_time_slot_min = (int(line.hour_from * 60) +
                                    duration_of_overview)
            time_to_min = int(line.hour_to * 60)
            start_hour = str(start_time_slot_min // 60)
            finish_hour = str(finish_time_slot_min // 60)
            if (int(start_hour) > 23 or start_time_slot_min < 0
                    or int(finish_hour) > 23 or time_to_min < 0
                    or start_time_slot_min > time_to_min):
                raise ValidationError(_('Problem with time'))
            while finish_time_slot_min <= time_to_min:
                start_hour = str(start_time_slot_min // 60)
                start_min = str(round(start_time_slot_min % 60 / 60 * 100))
                start_time = float(start_hour + '.' + start_min)
                finish_hour = str(finish_time_slot_min // 60)
                finish_min = str(round(finish_time_slot_min % 60 / 60 * 100))
                finish_time = float(finish_hour + '.' + finish_min)
                if self.env['service.center.slot'].search_count(
                        [('engineer_id', '=', engineer.id),
                         ('date', '=', line.date),
                         ('hour_from', '<=', start_time),
                         ('hour_to', '>', start_time)
                         ]):
                    pass
                else:
                    self.env['service.center.slot'].create({
                        'engineer_id': engineer.id,
                        'date': line.date,
                        'hour_from': start_time,
                        'hour_to': finish_time,
                    })
                start_time_slot_min += duration_of_overview
                finish_time_slot_min += duration_of_overview

    @api.depends('engineer_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.engineer_id.name}"
            )
