from odoo import api,fields,models


class DemoPractice(models.Model):
    _name='demo.practice'
    _description='This is a demo module'


    name = fields.Char(
        string='Name',
        required=False)

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=False)
    new_ids= fields.One2many(
        comodel_name='new.model',
        inverse_name='demo_id',
        string='new',
        required=False)

