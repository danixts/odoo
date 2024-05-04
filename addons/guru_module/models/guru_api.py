# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GuruApi(models.Model):
    _name = 'guru.api'
    _description = 'Modulo api'
    _rec_name = 'id'

    todo_id = fields.Integer(string='ID')
    title = fields.Char(string='Title')
    completed = fields.Boolean(string='Completed')

    def create_object(self, res):
        api_data = self.env['guru.api'].search([('todo_id', '=', res['id'])])
        if not api_data:
            self.create({
                "todo_id": res['id'],
                "title": res['title'],
                "completed": res['completed'],
            })

    def create_object_all(self, res):
        for todo in res:
            self.create_object(todo)
