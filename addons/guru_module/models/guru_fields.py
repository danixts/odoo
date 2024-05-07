# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class GuruFields(models.Model):
    _name = "guru.fields"
    _description = "Modulo fields"
    _rec_name = "result"

    value_a = fields.Float("Value A")
    value_b = fields.Float("Value B")
    multiple = fields.Float("Multiple Value")
    result = fields.Float("Result")
    result_modal = fields.Float("Result Modal")

    @api.onchange("value_a", "value_b", "multiple")
    def _onchange_sum_values(self):
        multiple = self.multiple or 0
        a = self.value_a * multiple or 0
        b = self.value_b * multiple or 0
        self.result = a * b

    @api.constrains("value_a")
    def _valid_value_a(self):
        if self.value_a < 0:
            raise ValidationError(_("Not valid field Valor A"))

    def handle_modal(self):
        self.ensure_one()
        return {
            "name": "Open Modal",
            "type": "ir.actions.act_window",
            "res_model": "guru.open.modal",
            "view_mode": "form",
            "context": {
                "default_value_a": self.value_a,
                "default_value_b": self.value_b,
                "default_user_id": self.env.user.id,
                "default_currency_id": self.env.company.currency_id.id,
                "other_value": "otro valor",
            },
            "target": "new",
        }
