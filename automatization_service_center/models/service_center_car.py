from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class ServiceCenterCar(models.Model):
    _name = 'service.center.car'
    _description = 'Cars of clients'
    """ This model is needed to store customers' cars
               """

    mark = fields.Char(
        required=True,
    )

    model = fields.Char(
        required=True,
    )

    year = fields.Char(

    )

    mileage = fields.Char(

    )

    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True,
    )

    photo = fields.Image(

    )

    @api.depends('mark', 'model')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = (
                f"{rec.mark}"
                f" {rec.model}"
            )

    @api.constrains('year')
    def _verify_car_year(self):
        """ this method creates a check that all characters are digits
        """
        for rec in self:
            if rec.year and not rec.year.isdigit():
                raise ValidationError(_("The Year must be"
                                        " a sequence of digits."))

    @api.constrains('mileage')
    def _verify_car_mileage(self):
        """ this method creates a check that all characters are digits
                """
        for rec in self:
            if rec.mileage and not rec.mileage.isdigit():
                raise ValidationError(_("The mileage must be"
                                        " a sequence of digits."))
