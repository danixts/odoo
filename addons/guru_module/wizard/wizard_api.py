# -*- coding: utf-8 -*-

from odoo import models, fields
import requests

from odoo.exceptions import ValidationError


class WizardOpenModal(models.TransientModel):
    _name = "guru.open.api"
    _description = "Wizard Open Api"

    todo_id = fields.Integer("Todo Id")

    def handle_button_click(self):
        res = self.service_fetch_all()
        if res:
            self.env["guru.api"].create_object_all(res)
            # return {
            #     'type': 'ir.actions.client',
            #     "tag": "reload"
            # }

    def service_fetch(self, id):
        try:
            res = requests.get(
                f"https://jsonplaceholder.typicode.com/todos/{id}",
                headers={"content-type": "application/json"},
            )
            res = res.json()
            return res
        except Exception as err:
            raise ValidationError(err)

    def service_fetch_all(self):
        try:
            res = requests.get(
                "https://jsonplaceholder.typicode.com/todos",
                headers={"content-type": "application/json"},
            )
            res = res.json()
            return res
        except Exception as err:
            raise ValidationError(err)
