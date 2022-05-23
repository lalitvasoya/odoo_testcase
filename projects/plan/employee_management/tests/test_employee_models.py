from datetime import datetime

from odoo.tests import common, tagged, Form


class TestEmployeeUserModel(common.TransactionCase):
    def test_on_change_(self):
        initial_value = {
            "name": "lalit",
            "email": "email",
            "doj": datetime.now(),
            "leave": 2,
            "height": 5.8,
            "summary": "python developer."
        }
        form = Form(self.env['employee.user'])
        for field, value in initial_value.items():
            setattr(form, field, value)
        record = form.save()
        self.assertEqual(record.salary, 14000)
        self.assertEqual(record.leave, 2)

