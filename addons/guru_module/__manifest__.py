# -*- coding: utf-8 -*-
{
    'name': "Guru Module",

    'summary': "Guru Base Module",

    'description': """
Guru Base Module
    """,

    'author': "Daniel",
    'website': "https://www.daniel.com",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'security/security_model.xml',
        'views/view_guru_model.xml',
        'views/view_guru_user.xml',
        'views/view_guru_fields.xml',
        'views/view_api.xml',

        'wizard/wizard_open_modal.xml',
        'wizard/wizard_api.xml',

        'report/report_action.xml',
        'report/report_template.xml',
        'views/view_menu.xml',
    ],
}
