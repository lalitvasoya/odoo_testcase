from odoo import fields, models


class Document(models.Model):

    _name = "document"
    _description = "Employee description"

    sequence = fields.Integer('Sequence')
    employee_id = fields.Many2one("employee.user", "Employee")
    name = fields.Char('Name', size=20)
    file = fields.Binary('File')
