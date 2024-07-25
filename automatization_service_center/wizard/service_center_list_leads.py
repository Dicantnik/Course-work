from odoo import models, fields


class ServiceCenterListLeads(models.TransientModel):
    _name = 'service.center.list.leads'
    _description = 'TransientModel for group and filter leads'

    engineer_ids = fields.Many2many(
        comodel_name="res.users",
        domain=[('is_engineer', '=', True)],
        required=True,
    )

    from_date = fields.Date(
        required=True
    )

    to_date = fields.Date(
        required=True
    )

    def action_submit_list_leads(self):
        domain = ["&", "&",
                  ("overview_slot_id.date", ">=", str(self.from_date)),
                  ("overview_slot_id.date", "<", str(self.to_date)),
                  ("engineer_id", "in", self.engineer_ids.ids)
                  ]
        return {
            'name': 'Leads',
            'model': 'ir.actions.act_window',
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'res_model': 'service.center.lead',
            'domain': domain,
            'type': 'ir.actions.act_window',
        }
