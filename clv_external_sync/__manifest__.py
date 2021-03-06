# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'External Sync',
    'summary': 'External Sync Module used by CLVsol Solutions.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
    ],
    'data': [
        'security/external_sync_security.xml',
        'security/ir.model.access.csv',
        'views/external_sync_host_view.xml',
        'views/external_sync_view.xml',
        'views/external_sync_template_view.xml',
        'views/external_sync_schedule_view.xml',
        'views/external_sync_object_field_view.xml',
        'views/external_sync_batch_view.xml',
        'views/external_sync_batch_member_view.xml',
        'views/referenceable_model_view.xml',
        'data/external_sync_batch_member.xml',
        'data/external_sync_batch_member_seq.xml',
        'data/external_sync.xml',
        'wizard/external_sync_mass_edit_view.xml',
        'wizard/external_sync_template_mass_edit_view.xml',
        'wizard/external_sync_schedule_mass_edit_view.xml',
        'wizard/external_sync_schedule_exec_view.xml',
        'wizard/external_sync_schedule_exec_2_view.xml',
        'wizard/external_sync_batch_exec_view.xml',
        'wizard/external_sync_batch_member_mass_edit_view.xml',
        'wizard/external_sync_schedule_mass_edit_2_view.xml',
        'views/external_sync_menu_view.xml',
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
