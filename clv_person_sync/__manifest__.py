# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Person External',
    'summary': 'Person External Sync Module used by CLVsol Solutions.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_person',
        'clv_external_sync',
    ],
    'data': [
        # 'data/person_age_range.xml',
        'data/person_age_range_sync.xml',
        'data/person_category_sync.xml',
        'data/person_marker_sync.xml',
        'data/person_sync.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
