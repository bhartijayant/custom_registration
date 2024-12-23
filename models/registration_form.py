from odoo import models, fields

class RegistrationForm(models.Model):
    _name = 'registration.form'  # Keep this to match ir.model.access.csv
    _description = 'Family Welfare Program'

    family_name = fields.Char(string="Family Name", required=True)
    address = fields.Char(string="Address", required=True)
    num_members = fields.Integer(string="Number of Members", required=True)
    monthly_income = fields.Float(string="Monthly Income", required=True)
    additional_notes = fields.Text(string="Additional Notes")