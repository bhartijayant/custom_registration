from odoo import models, fields

class EducationBenefit(models.Model):
    _name = 'education.benefit'
    _description = 'Children Education Benefit Program'

    child_name = fields.Char(string="Child's Name", required=True)
    parent_name = fields.Char(string="Parent/Guardian Name", required=True)
    school_name = fields.Char(string="School Name", required=True)
    grade = fields.Char(string="Grade/Class", required=True)
    date_of_application = fields.Date(string="Date of Application", required=True)
    benefit_amount = fields.Float(string="Benefit Amount", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string="Application Status", default='draft')
    is_approved = fields.Boolean(string="Is Approved?", default=False)
    comments = fields.Html(string="Additional Comments")