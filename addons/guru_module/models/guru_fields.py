# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GuruFields(models.Model):
    _name = 'guru.fields'
    _description = 'Modulo fields'
    _rec_name = 'result'

    value_a = fields.Float('Value A')
    value_b = fields.Float("Value B")
    multiple = fields.Float("Multiple Value")
    result = fields.Float("Result")

    @api.onchange("value_a", "value_b", "multiple")
    def _onchange_sum_values(self):
        multiple = self.multiple or 0
        a = self.value_a * multiple or 0
        b = self.value_b * multiple or 0
        self.result = a + b
