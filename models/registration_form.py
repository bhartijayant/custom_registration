from odoo import models, fields
 
class RegistrationForm(models.Model):
    _name = 'registration.form'
    _description = 'Registration Form'
 
    name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    address = fields.Text(string='Address')
    # dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    occupation = fields.Text(string='Occupation')  # New Occupation field
