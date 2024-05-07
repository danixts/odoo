# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WizardOpenModal(models.TransientModel):
    _name = "guru.open.modal"
    _description = "Wizard Open Modal"

    value_a = fields.Float("Value A")
    value_b = fields.Float("Value B")

    user_id = fields.Many2one("res.users", string="User")
    currency_id = fields.Many2one("res.currency", string="Currency")

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        # res['user_id'] = self._context.get('uid')
        # print('.............', self._context.get('other_value'))
        return res

    def handle_button_click(self):
        # search
        # search_read
        # browse
        # search_count

        # [('nombre del campo','exp', 'valor a buscar'),('user_id','=',1)]
        ### exp
        # = compara si es igual
        # > < comparacion de valores numericos
        # != diferente de
        # in [1,2,3,4] => para buscar multiples valores
        # not in => negacion
        # like => para buscar cadenas
        ###

        # SQL SELECT * FROM guru_fields WHERE user_id = 1 or user_id = 2
        active_id = self._context.get("active_id")
        model_active = self.env["guru.fields"].search([("id", "=", active_id)])
        if model_active:
            suma = self.value_a + self.value_b
            model_active.write(
                {
                    "result_modal": suma,
                }
            )
            guru_model = self.env["guru.model"].create(
                {
                    "is_active": True,
                    "first_name": "Modal",
                    "last_name": "Popup",
                    "age": 2,
                    "amount": 200,
                    "user_id": self.env.user.id,
                    # "note": F'Desde mi modal la suma es {suma}'
                }
            )
            guru_model.press_button()
            print("CREATE OBJECT", guru_model)
            # self.env['res.partner'].create({
            #     "name": "USUARIO PRUEBA"
            # })
