# -*- coding: utf-8 -*-
{
    'name': "Available Drivers",
    'version': '17.0.1.0.0',
    'category': 'Project',
       'summary': """Get all available drivers for the task at given time and date""",
    'description': """This module helps to find out the available drivers for a
     project task based on the task start,end date and time.""",
    'author': 'AMV',
    'company': 'Amevia s.r.o.',
    'maintainer': 'AMV',
    'website': "www.amevia.eu",
    'depends': ['project', 'hr_timesheet'],
    'data': [
    'security/ir.model.access.csv',
    'views/project_task_views.xml',
    'views/res_users_views.xml',
    'wizards/available_drivers_views.xml'  
],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

