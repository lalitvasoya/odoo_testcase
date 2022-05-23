from odoo import fields, models


todo_status_choices = [
    ("pending", "Pending"),
    ("in progress", "In-Progress"),
    ("done", "Done")
]


class Todo(models.Model):

    _name = 'todo'

    task = fields.Char("task", size=20)
    status = fields.Selection(selection=todo_status_choices)
