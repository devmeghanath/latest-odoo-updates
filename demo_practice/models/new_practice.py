from odoo import api, fields, models


class NewPractice(models.Model):
    _name = "new.model"


    demo_id = fields.Many2one(
        comodel_name='demo.practice',
        string='Demo',
        required=False)