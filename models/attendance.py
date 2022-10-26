from odoo import fields, models, api


class InheritedAttendance(models.Model):
    _inherit = "hr.attendance"

    agence = fields.Char(string="Agence", readonly=True)

    @api.model
    def create(self, values):
        self.agence = self.env.user.company_id.street
        override_create = super(InheritedAttendance, self).create(values)
        return override_create

    @api.multi
    def write(self, values):
        self.agence = self.env.user.company_id.street
        override_write = super(InheritedAttendance, self).write(values)
        return override_write
