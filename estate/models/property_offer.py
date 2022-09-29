from odoo import api, fields, models
import datetime
from odoo.exceptions import UserError
class PropertyOffer(models.Model):
    _name = 'property.offer'
    _description = 'PropertyOffer'
    _order = "price desc"

    create_date = fields.Date(
        string='Create date',
        required=False)

    price = fields.Float(
        string='Price', 
        required=False)
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'),
                   ('reffused', 'Reffused'), ],
        required=False,
        copy=False)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner_id',
        required=True)
    property_id = fields.Many2one(
        comodel_name='estate.property',
        string='Property_id',
        required=True)
    property_type_id = fields.Many2one(
        related='property_id.property_type_id',
        string="Property_type",
        required=False)
    status_of_property = fields.Integer(
        string='Status_of_property',
        related='property_id.current_status',
        required=False)
    validity = fields.Integer(
        string='Validity',
        default=7,
        required=False)
    date_deadline = fields.Date(
        string='Date deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
        required=False)


    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date != False:
                record.date_deadline = (record.create_date + datetime.timedelta(days=record.validity))

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline != False:
                record.validity = (record.date_deadline - record.create_date).days

    def action_accept(self):
        if self.property_id.current_status != 1:
            self.property_id.buyer = self.partner_id.name
            self.property_id.selling_price = self.price
            self.status = 'accepted'
            self.property_id.state = 'offer_accepted'
            self.property_id.current_status = 1
    def action_reject(self):
        if self.status == 'accepted':
            self.property_id.state='new'
            self.status = 'reffused'
            self.property_id.current_status =0;
        else:
            self.status = 'reffused'
    # @api.depends('status')
    # def _onchange_status(self):
    #     print('-------------------->',self.status)
    #     if self.status == 'accepted':
    #         self.property_id.state = 'accepted'
    #         print(self.property_id.state)

    @api.model
    def create(self,vals):

        res=super(PropertyOffer, self).create(vals)
        self.env['estate.property'].browse(vals['property_id']).write({'state':'offer_accepted'})
        prices=max(self.env['estate.property'].browse(vals['property_id']).offer_ids.mapped('price'))
        if vals['price']<prices:
            raise UserError('canot careate offer less than current offer')
        return res










