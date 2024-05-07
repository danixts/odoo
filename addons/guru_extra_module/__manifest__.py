# -*- coding: utf-8 -*-
{
    'name': "Guru Extra Module",
    'summary': "Guru Extra Module",
    'description': """Guru Extra Module""",
    'author': "Daniel",
    'website': "https://www.daniel.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['guru_module', 'point_of_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/view_guru_model.xml',
        'views/view_res_partner.xml',
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            "guru_extra_module/static/src/js/EditPartner.js",
            "guru_extra_module/static/src/js/Model.js",

            "guru_extra_module/static/src/xml/EditPartner.xml",
        ]
    }
}
