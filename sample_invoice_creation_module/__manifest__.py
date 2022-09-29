{
    'name': 'sample invoice',
    'version': '',
    'summary': '',
    'description': 'for create a invoice',
    'depends': ['base','account','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/base.view.xml',
        'views/menu.xml',
        'views/inherited_view_report.xml',
        'report/report.xml',
        'report/report_template.xml',

           ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}