{
    'name': 'ITQ Trip Request',
    'version': '0.1',
    'author': "Itqan Systems",
    'website': "http://www.itqansystems.com",
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_contract',

    ],

    # always loaded
    'data': [
        # Security files:
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        # Data files:

        # Root menu items files:

        # View files:
        'views/employee_view.xml',
        'views/itq_mina_trip_request.xml',
        'reports/report.xml',
        # Menu items files:


    ],
    'installable': True
}
