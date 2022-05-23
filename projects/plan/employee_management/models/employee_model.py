from odoo import fields, models, api


employee_status_choices = [
    ('draft', "New"),
    ('pending_approval', 'Send For Approval'),
    ('employee', 'Employee'),
    ('not_a_employee', 'Left')
]


class EmployeeUser(models.Model):

    _name = 'employee.user'

    # basic fields
    name = fields.Char('Name', size=20, help="Please enter the employee name.")
    email = fields.Char('Email', size=30, help="Please enter the email")
    doj = fields.Date("DOJ")
    leave = fields.Integer("Leave")
    height = fields.Float("Height")
    salary = fields.Float('Salary', compute='_compute_salary', inverse='_inverse_salary', default=15000)
    active = fields.Boolean("Active", default=True)
    summary = fields.Text("Summary")
    state = fields.Selection(selection=employee_status_choices, string='Status', default='draft')

    # relational fields
    company_id = fields.Many2one('employee.company', string="Company")
    document_ids = fields.One2many('document', 'employee_id', string="Document")
    hobbies_ids = fields.Many2many(comodel_name='hobby', relation='employee_hobby_rel',
                                   column1='emp_id', column2='hobby_id', string='Hobbies')
    company_is_active = fields.Boolean("Company is active", related="company_id.is_active")

    @api.depends("leave")
    def _compute_salary(self):
        for record in self:
            record.salary = 15000 - (15000 * record.leave) / 30

    def _inverse_salary(self):
        for record in self:
            record.leave = 30 - (record.salary * 30) / 15000

    @api.onchange("name")
    def onchange_name(self):
        if self.name:
            self.summary = self.name + " is Tntra employee."

    def send_for_approval(self):
        self.state = 'pending_approval'

    def make_employee(self):
        self.state = 'employee'

    def leaving_company(self):
        self.state = 'not_a_employee'

    def reset(self):
        self.state = "draft"
