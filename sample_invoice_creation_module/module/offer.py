from odoo import api, fields, models


class OfferModule(models.Model):
    _name = 'offer.module'



    price = fields.Integer(
        string='Price',
        required=False)
