from odoo import api, fields, models
from random import randint


class PropertyTag(models.Model):
    _name = 'property.tag'
    _description = 'PropertyTag'
    _order = "name"


    name = fields.Char(required=True)

    def _get_default_color(self):
        return randint(1, 11)
    color = fields.Integer(
        string='Color',
        default=lambda self: self._get_default_color())

