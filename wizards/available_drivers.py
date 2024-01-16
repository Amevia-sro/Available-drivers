# -*- coding: utf-8 -*-

from odoo import fields, models

class AvailableDrivers(models.TransientModel):
    _name = 'available.drivers'
    _description = 'Wizard to find available drivers within a specified period'

    Journey_start_date = fields.Datetime(string="Journey Start Date", help="Start date and time of the journey")
    Journey_end_date = fields.Datetime(string="Journey End Date", help="End date and time of the journey")

    def get_available_drivers(self):
        """Get the list of available drivers at the given period"""
        start_date = self.Journey_start_date
        end_date = self.Journey_end_date

        if start_date and end_date:
            case = 'not in'
            driver_ids = self.env['project.task'].get_available_driver_ids(start_date, end_date)
            user_ids = driver_ids
        else:
            case = 'in'
            user_ids = []

        return {
            'name': 'Available Drivers',
            'view_mode': 'tree,form',
            'target': 'main',
            'res_model': 'res.users',
            'views': [
              (self.env.ref('available_drivers.res_users_view_tree').id, 'tree'),
              (self.env.ref('available_drivers.res_users_view_form').id, 'form')],
            'type': 'ir.actions.act_window',
            'domain': [('id', case, user_ids), ('share', '=', False)],
        }

