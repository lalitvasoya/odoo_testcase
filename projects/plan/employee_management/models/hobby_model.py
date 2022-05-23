from odoo import fields, models


class Hobby(models.Model):

    _name = 'hobby'
    _description = 'users hobbies'

    name = fields.Char('Name')
    rate = fields.Integer('Rate')
