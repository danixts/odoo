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
        'views/view_guru_model.xml',
        'views/view_guru_user.xml',
        'views/view_menu.xml',
    ],
}
