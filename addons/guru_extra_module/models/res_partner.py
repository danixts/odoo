from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    pin_code = fields.Char(string="Pin Code")
