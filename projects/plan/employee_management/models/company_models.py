from odoo import fields, models


class EmployeeCompany(models.Model):

    _name = 'employee.company'
    _description = "Employee Company"

    name = fields.Char("Name", size=50)
    is_active = fields.Boolean("Active", default=True)
