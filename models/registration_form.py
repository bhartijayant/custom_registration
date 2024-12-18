from odoo import models, fields

class RegistrationForm(models.Model):
    _name = 'registration.form'
    _description = 'Simple Registration Form'

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)