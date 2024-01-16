# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProjectTask(models.Model):
    _inherit = 'project.task'

    Journey_start_date = fields.Datetime(string="Journey Start Date", required=True, help='Start date and time of the journey')
    Journey_end_date = fields.Datetime(string="Journey End Date", required=True, help='End date and time of the journey')
    users_ids = fields.Many2many('res.users', compute="_compute_users_ids", help="Users available for the task")
    manager_id = fields.Many2one('res.users', string='Manager')

    @api.depends('Journey_start_date', 'Journey_end_date', 'project_id.message_follower_ids', 'users_ids')
    def _compute_users_ids(self):
        for record in self:
            if record.Journey_end_date and record.Journey_start_date:
                start_date = record.Journey_start_date
                end_date = record.Journey_end_date
                driver_ids = self.get_available_driver_ids(start_date, end_date)
                domain = [('id', 'not in', driver_ids), ('share', '=', False)]
                if record.project_id.privacy_visibility == 'followers':
                    domain.append(('id', 'in', record.project_id.message_follower_ids.ids))
                record.users_ids = self.env['res.users'].search(domain)

    @api.depends('users_ids')
    def _compute_manager_id(self):
        for record in self:
            if record.users_ids:
                # Set manager_id to the first user in users_ids
                record.manager_id = record.users_ids[0]

    def get_available_driver_ids(self, start_date, end_date):
        """ Get the available drivers for the particular period """
        driver_ids = []
        tasks = self.env['project.task'].search([
            '|',
            '&', ('Journey_start_date', '<=', start_date), ('Journey_end_date', '>=', start_date),
            '&', ('Journey_start_date', '<=', end_date), ('Journey_end_date', '>=', end_date)
        ])
        for task in tasks:
            if task.manager_id:
                driver_ids.append(task.manager_id.id)
            driver_ids.extend(task.users_ids.ids)
        return list(set(driver_ids))

