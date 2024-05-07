# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    # is_active = fields.Boolean(string='Active')
    ref_internal = fields.Char(string="Internal Reference", size=10, required=True)
