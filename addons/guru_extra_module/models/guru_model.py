from odoo import models, fields


class GuruModule(models.Model):
    _inherit = "guru.model"

    key_id = fields.Char(string="Key ID")

    def press_log(self):
        super().press_log()
        guru_model = self.env["guru.model"].search_read(
            fields=["id", "first_name", "last_name", "note", "is_active", "user_id"],
            domain=[("is_active", "=", True)],  # where
        )
        print("DESDE PRESLOG EXTRA MODULE", guru_model)

    def press_extra_module(self):
        print("MODULE EXTRA", self.id)
