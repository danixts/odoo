# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

STATUS_VALUES = [
    ('draft', 'Draft'),
    ('pending', 'Pending'),
    ('done', 'Done'),
]

_logger = logging.getLogger(__name__)


class GuruModule(models.Model):
    _name = 'guru.model'
    _description = 'Modulo base guru'
    _rec_name = 'first_name'

    is_active = fields.Boolean('Is Active', default=False)
    first_name = fields.Char('First Name', required=True, translate=True)
    last_name = fields.Char('Last Name', required=True, translate=True)
    age = fields.Integer("Age")
    amount = fields.Float("Amount", default=0)
    status = fields.Selection(STATUS_VALUES, default='draft')
    user_id = fields.Many2one('res.users', string='User')
    users_ids = fields.Many2many('guru.user', string='Users')
    note = fields.Text('Note')

    @api.depends('first_name', 'last_name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s %s" % (rec.first_name or "", rec.last_name or "")

    def create(self, values):
        if values.get('first_name', False) and values.get('last_name', False):
            values['is_active'] = True
        values['user_id'] = self.env.user.id
        values['status'] = 'pending'
        _logger.error('CREATE MODEL -> %s', values)
        return super().create(values)

    def press_log(self):
        _logger.info(f'DESDE PRES_LOG {self.first_name} {self.last_name}')
        # query = "select name, symbol, full_name from res_currency rc where active is true;"
        query = "select id, first_name, last_name, note, is_active from guru_model where is_active is true order by id;"
        self.env.cr.execute(query)
        guru_model = self.env.cr.fetchall()
        response = []
        for model in guru_model:
            id, first_name, last_name, note, is_active = model
            response.append({
                'id': id,
                'first_name': first_name,
                'last_name': last_name,
                'note': note,
                'is_active': is_active,
            })

        # self.env.cr.commit()
        print(response)

    def print_pdf(self):
        return self.env.ref('guru_module.action_guru_model').report_action(self)

    def press_button(self):
        context = self._context.get('active_model', False)
        if context == 'guru.fields':
            self.write({
                "note": "desde mi modal"
            })
            return

        users = []
        for rec in self.users_ids:
            payload = {
                "names": "%s %s" % (rec.first_name, rec.last_name),
                "email": rec.email,
                "phone": rec.phone,
                "gender": rec.gender,
                "currency_id": {
                    "id": rec.currency_id.id,
                    "name": rec.currency_id.name,
                }
            }
            users.append(payload)

        self.write({
            "note": users
        })
        _logger.info(users)
