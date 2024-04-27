# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GuruModule(models.Model):
    _name = 'guru.model'
    _description = 'Modulo base guru'
    _rec_name = 'first_name'

    is_active = fields.Boolean('Is Active', default=False)
    first_name = fields.Char('First Name', required=True, translate=True)
    last_name = fields.Char('Last Name', required=True, translate=True)
    age = fields.Integer("Age")
    amount = fields.Float("Amount", default=0)

    @api.depends('first_name', 'last_name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s %s" % (rec.first_name or "", rec.last_name or "")

    def create(self, values):
        if values.get('first_name', False) and values.get('last_name', False):
            values['is_active'] = True
        return super().create(values)
