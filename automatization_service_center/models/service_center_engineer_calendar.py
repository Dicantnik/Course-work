from odoo import models, fields


class ServiceCenterTimeTable(models.Model):
    _name = 'service.center.engineer.calendar'
    _description = 'Model for calendar of engineers'
    """ This model is needed to store on what day from what time
     and until what time the engineer will inspect the machines
               """

    time_table_id = fields.Many2one(
        comodel_name='service.center.time.table'
    )

    date = fields.Date(
        string='Working date',
        required=True
    )

    hour_from = fields.Float(
        string='Work from',
        required=True,
    )

    hour_to = fields.Float(
        string='Work to',
        required=True
    )
