# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReportGuruModel(models.AbstractModel):
    # report . nombre modulo . id reporte
    _name = 'report.guru_module.report_guru_model'
    _description = 'Report Module'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['guru.model'].browse(docids)
        model_fields = self.env['guru.fields'].search([('id', '=', 2)])
        return {
            "doc_ids": docids,
            "docs": docs,
            "fields": model_fields,
        }
