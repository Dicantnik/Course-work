from odoo import models, fields


class ServiceCenterService(models.Model):
    _name = 'service.center.service'
    _description = 'Model for services'
    """ This model is needed to store services
               """

    name = fields.Char(
        required=True,
    )

    duration = fields.Float(
        required=True,
    )

    price = fields.Integer(
        required=True,
    )

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        required=True,
    )
