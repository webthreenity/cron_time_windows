{
    'name': 'Cron Time Windows - Cron Scheduler for Business Hours & Fixed Times',
    'version': '18.0.1.0.0',
    'summary': 'Scheduled actions scheduler: run each cron only within time windows '
               '(business hours, office hours, pause at night) with its own frequency '
               'per window, or at fixed times daily, weekly and monthly. Cron '
               'timezone and daylight saving aware, templates, apply to many '
               'scheduled actions at once',
    'category': 'Extra Tools',
    'author': 'WebThreenity',
    'website': 'https://webthreenity.netlify.app',
    'support': 'elouafiabderrahmane2002@gmail.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ir_cron_views.xml',
        'views/cron_tw_template_views.xml',
        'wizard/cron_tw_wizard_views.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
}
