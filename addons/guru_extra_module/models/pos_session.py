from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        res = super()._loader_params_res_partner()
        fields_data = ['pin_code']
        for field in fields_data:
            res["search_params"]["fields"].append(field)
        return res

    def get_data_guru(self):
        guru_model = self.env['guru.model'].search_read(
            fields=['id', 'first_name', 'last_name', 'note', 'is_active', 'user_id'],
            domain=[("is_active", "=", True)]  # where
        )
        return guru_model
