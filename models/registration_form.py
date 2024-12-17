from odoo import models, fields

class RegistrationForm(models.Model):
    _name = 'registration.form'  # Revert to match ir.model.access.csv
    _description = 'Girl Child Education and Welfare Program'

    # Basic Information
    child_name = fields.Char(string="Girl's Full Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    parent_name = fields.Char(string="Parent/Guardian Name", required=True)
    school_name = fields.Char(string="School Name", required=True)
    grade = fields.Selection(
        [(str(i), f"Class {i}") for i in range(1, 12)],
        string="Grade/Class",
        required=True
    )
    date_of_application = fields.Date(string="Date of Application", required=True)

    # Financial Details
    family_income = fields.Float(string="Annual Family Income", required=True)
    education_expenses = fields.Float(string="Annual Education Expenses", required=True)
    scholarship_details = fields.Text(string="Scholarship Details")
    additional_notes = fields.Text(string="Additional Notes")

    # Parent/Guardian Details
    parent_occupation = fields.Selection([
        ('salaried', 'Salaried'),
        ('self_employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('student', 'Student'),
        ('retired', 'Retired'),
    ], string="Parent Occupation", required=True)
    is_single_parent = fields.Boolean(string="Is Single Parent?", default=False)
    residence_type = fields.Selection([
        ('own', 'Own House'),
        ('rented', 'Rented House'),
        ('other', 'Other'),
    ], string="Residence Type", required=True)

    # Application Status
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string="Application Status", default='draft')
    is_approved = fields.Boolean(string="Approved", default=False)