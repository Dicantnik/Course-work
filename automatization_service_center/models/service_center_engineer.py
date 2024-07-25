from odoo import models, fields


class ServiceCenterResPartner(models.Model):
    _inherit = 'res.users'
    _description = 'Model for Engineers'
    """ This model extends the res.users model
     and adds a marker for whether I am an engineer
               """

    is_engineer = fields.Boolean(

    )
