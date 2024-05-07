from odoo import models, fields, api

# TUPLAS
# ('lunes', 'martes', 'miercoles', 'jueves')

# [('key', 'value'),('key', 'value'),('key', 'value'),('key', 'value')]

GENDER_VALUES = [
    ("M", "Masculino"),
    ("F", "Femenino"),
    ("O", "Otro"),
]


class GuruUser(models.Model):
    _name = "guru.user"
    _description = "Modulo user"
    _inherit = ["mail.thread"]

    first_name = fields.Char("First Name", required=True, tracking=True)
    last_name = fields.Char("Last Name", required=True, tracking=True)
    image = fields.Image("Image")
    email = fields.Char("Email", tracking=True)
    phone = fields.Char("Phone", tracking=True)
    nit = fields.Char("Nit", required=True)
    status = fields.Boolean("Status", tracking=True)
    birth_date = fields.Date("Birth Date", default=fields.Date.today)
    gender = fields.Selection(GENDER_VALUES)
    note = fields.Text("Note")

    currency_id = fields.One2many("guru.currency", "guru_user_id", "Currency")

    @api.depends("first_name", "last_name")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s %s" % (rec.first_name or "", rec.last_name or "")

    # self.message_post(body=message)
