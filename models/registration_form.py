from odoo import models, fields

class RegistrationForm(models.Model):
    _name = 'registration.form'
    _description = 'Children Education Benefit Program'

    child_name = fields.Char(string="Child's Name", required=True)
    parent_name = fields.Char(string="Parent/Guardian Name", required=True)
    school_name = fields.Char(string="School Name", required=True)
    grade = fields.Selection(
        [(str(i), f"Class {i}") for i in range(1, 13)],
        string="Grade/Class",
        required=True
    )
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

    # New Fields
    parent_occupation = fields.Selection([
        ('salaried', 'Salaried'),
        ('self_employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('student', 'Student'),
        ('retired', 'Retired'),
    ], string="Parent/Guardian Occupation", required=True)
    family_income = fields.Float(string="Annual Family Income", required=True)
    num_children = fields.Integer(string="Number of Children in Family", required=True)
    is_single_parent = fields.Boolean(string="Single Parent?", default=False)
    residence_type = fields.Selection([
        ('own', 'Own House'),
        ('rented', 'Rented House'),
        ('other', 'Other'),
    ], string="Residence Type", required=True)
    education_expenses = fields.Float(string="Education Expenses (Yearly)", required=True)
    income_proof = fields.Binary(string="Upload Income Proof")
    loan_status = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string="Currently Paying Any Loan?")
    loan_details = fields.Text(string="Loan Details (if any)")
    additional_notes = fields.Text(string="Additional Notes")