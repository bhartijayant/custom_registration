from odoo import models, fields

class GirlChildEducation(models.Model):
    _name = 'girl.child.education'
    _description = 'Girl Child Education and Welfare Program'

    # Basic Information
    child_name = fields.Char(string="Girl's Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    parent_name = fields.Char(string="Parent/Guardian Name", required=True)
    school_name = fields.Char(string="School Name", required=True)
    grade = fields.Selection(
        [(str(i), f"Class {i}") for i in range(1, 13)],
        string="Grade/Class",
        required=True
    )
    date_of_application = fields.Date(string="Date of Application", required=True)

    # Financial Details
    family_income = fields.Float(string="Annual Family Income", required=True)
    benefit_amount_requested = fields.Float(string="Requested Benefit Amount", required=True)
    benefit_amount_approved = fields.Float(string="Approved Benefit Amount", readonly=True)
    monthly_expenses = fields.Float(string="Monthly Expenses", required=False)

    # Parent/Guardian Details
    parent_occupation = fields.Selection([
        ('salaried', 'Salaried'),
        ('self_employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('student', 'Student'),
        ('retired', 'Retired'),
    ], string="Parent/Guardian Occupation", required=True)
    is_single_parent = fields.Boolean(string="Single Parent?", default=False)
    residence_type = fields.Selection([
        ('own', 'Own House'),
        ('rented', 'Rented House'),
        ('other', 'Other'),
    ], string="Residence Type", required=True)

    # Education and Welfare Specific Details
    education_expenses = fields.Float(string="Education Expenses (Yearly)", required=True)
    scholarship_details = fields.Text(string="Scholarship Details")
    extracurricular_activities = fields.Text(string="Extracurricular Activities")
    medical_support_details = fields.Text(string="Medical Support Details", required=False)

    # Supporting Documents
    income_proof = fields.Binary(string="Upload Income Proof")
    birth_certificate = fields.Binary(string="Upload Birth Certificate")
    school_certificate = fields.Binary(string="Upload School Certificate")
    additional_documents = fields.Binary(string="Additional Supporting Documents")

    # Application Status
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string="Application Status", default='draft')
    is_approved = fields.Boolean(string="Is Approved?", default=False)

    # Additional Notes
    additional_notes = fields.Text(string="Additional Notes")