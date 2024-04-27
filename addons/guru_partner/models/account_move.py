# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    type_document = fields.Char("Document Type", size=20, default="CI")
