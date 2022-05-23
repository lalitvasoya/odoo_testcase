from datetime import datetime

from odoo.tests import common, tagged


class TestEmployeeUserModel(common.TransactionCase):
    def test_on_change_(self):
        initial_value = {
            "name": "lalit",
            "email": "email",
            "doj": datetime.now(),
            "leave": 2,
            "height": 5.8,
            "salary": 15000,
            "summary": "python developer."
        }
        record = self.env['employee.user'].create(initial_value)
        record._onchange_name()
        breakpoint()
