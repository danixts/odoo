# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GuruCurrency(models.Model):
    _name = 'guru.currency'
    _description = 'Modulo guru currency'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code', size=10)

    user_id = fields.Many2one('res.users', string='User')
    currency_id = fields.Many2one('res.currency', string='Currency')

    # One2Many - relacion inversa
    guru_user_id = fields.Many2one('guru.user', string='User Guru')
