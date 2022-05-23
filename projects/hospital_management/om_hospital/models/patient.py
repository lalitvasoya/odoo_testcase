from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    # _inherit = "mail.thread"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    ref = fields.Char(string="Reference")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')])
    active = fields.Boolean(string="Active", default=True)
