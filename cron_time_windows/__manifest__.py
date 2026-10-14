{
    'name': 'Cron Time Windows | Cron Scheduler | Cron Job Business Hours | Scheduled Actions at Fixed Times',
    'version': '19.0.1.0.1',
    'summary': 'Cron job scheduler for Odoo scheduled actions (ir.cron): run each '
               'cron only during business hours, office hours or working hours, with '
               'its own frequency per time window, pause it at night or on weekends, '
               'or run it at fixed times: daily, weekly or monthly at a specific '
               'time. Cron timetable with timezone and daylight saving support, '
               'templates, apply to many scheduled actions at once. Also: cron time '
               'handler, cron interval, schedule a cron job, scheduled jobs, time '
               'window scheduler',
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
