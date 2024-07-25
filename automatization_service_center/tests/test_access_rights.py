from odoo.addons.automatization_service_center.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'access')
class TestAccessRights(TestCommon):

    def test_01_service_center_user_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['service.center.lead'].with_user(
                self.service_center_user
            ).create({
                'car_id': self.car
            })
        self.car.with_user(self.service_center_user).unlink()

    def test_02_service_center_admin_access_rights(self):
        lead = self.env['service.center.lead'].with_user(
            self.service_center_admin
        ).create({
            'car_id': self.car.id
        })
        lead.with_user(self.service_center_admin).read()
        lead.with_user(self.service_center_admin).write({
            'comment': 'Need to look more'
        })
        lead.with_user(self.service_center_admin).unlink()
