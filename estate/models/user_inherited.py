from odoo import api, fields, models
class ResUser(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='user_id',
        string='Property ',
        required=False)
    required = fields.Boolean(
        string='Active',
        required=False
    )
    property_type_id = fields.Many2one(
        comodel_name='property.type',
        string='Property Type',
        required=False)


