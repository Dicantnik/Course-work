from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_service_center_user = self.env.ref(
            'automatization_service_center.group_service_center_user')
        self.group_service_center_admin = self.env.ref(
            'automatization_service_center.group_service_center_admin')

        self.service_center_user = self.env['res.users'].create({
            'name': 'Service Center User',
            'login': 'service_center_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_service_center_user.id)],
        })

        self.service_center_admin = self.env['res.users'].create({
            'name': 'Service Center Admin',
            'login': 'service_center_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_service_center_admin.id)],
        })
        self.car = self.env['service.center.car'].create({
            'mark': 'Skoda',
            'model': 'Octavia',
            'res_partner_id': self.service_center_user.partner_id.id,
        })
