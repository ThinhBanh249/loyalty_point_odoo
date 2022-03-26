# -*- coding: utf-8 -*-
{
    'name': "loyalty_program",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/phan_quyen.xml',
        'views/loyalty_email_template.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/res_config_settings_views.xml',
        'views/loyalty_program_views.xml',
        'views/res_partner_view.xml',
        'views/loyalty_history_views.xml',
        'views/partner_level_views.xml',
        'views/sale_order_views.xml',
        'views/menus.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}
