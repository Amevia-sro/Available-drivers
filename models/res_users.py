# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    """To know the assigned/available drivers"""
    _inherit = 'res.users'

    project_allocated_ids = fields.One2many(comodel_name='project.task',
                                            inverse_name='user_ids',
                                            string='Assigned Drivers',  # Updated field string
                                            help='The drivers who are assigned')  # Updated help text
