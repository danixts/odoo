# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api, http
from odoo.http import Response, request


class ApiController(http.Controller):
    @http.route('/api/v1/GuruModel', auth='public', methods=['GET'], csrf=False)
    def get_guru_model(self, **kw):
        guru_model = request.env['guru.model'].search_read(
            fields=['id', 'first_name', 'last_name', 'note', 'is_active', 'user_id'],
            domain=[("is_active", "=", True)]  # where
        )
        return Response(json.dumps({
            "data": guru_model,
            "success": True,
            "errorCode": "C000",
            "message": "Service Guru Model Ok"
        }), content_type='application/json', status=404)

    # def get_guru_model(self, **kw):
    #     try:
    #         query = "select id, first_name, last_name, note, is_activ from guru_model where is_active is true order by id;"
    #         request.cr.execute(query)
    #         guru_model = request.cr.fetchall()
    #         response = []
    #         for model in guru_model:
    #             id, first_name, last_name, note, is_active = model
    #             response.append({
    #                 'id': id,
    #                 'first_name': first_name,
    #                 'last_name': last_name,
    #                 'note': note,
    #                 'is_active': is_active,
    #             })
    #         return Response(json.dumps({
    #             "data": response,
    #             "success": True,
    #             "errorCode": "C000",
    #             "message": "Service Guru Model Ok"
    #         }), content_type='application/json', status=404)
    #     except Exception as err:
    #         return Response(json.dumps({
    #             "error": "Service Error Data"
    #         }), content_type='application/json', status=500)
