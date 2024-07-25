from odoo import models, fields


class ServiceCenterResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Model for Clients'
    """ This model is needed to save customers of the service center
        and added a field to view all customer machines
           """

    car_ids = fields.One2many(
        comodel_name='service.center.car',
        inverse_name='res_partner_id'
    )
