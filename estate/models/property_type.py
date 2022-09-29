from odoo import api, fields, models


class PropertyType(models.Model):

    _name = 'property.type'
    _description = 'PropertyType is for mentioning the property type of each property'
    _order = " sequence, name"

    name = fields.Char(required=True)
    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='property_type_id',
        string='Property ids',
        required=False)
    sequence = fields.Integer('sequence', default=1)
    note_taker = fields.Html(
        string='Note taker',
        required=False)
    hide_name = fields.Boolean(
        string='Hide Name',

    )

    product_new_id = fields.Many2one(comodel_name = 'product.template',
                                 string = 'product name')
    # offer_ids = fields.One2many(
    #     comodel_name='property.offer',
    #     inverse_name='property_type_id',
    #     string='Offer ids',
    #     required=False)

   
    offer_count = fields.Integer(
        string='Offer count',
        compute='_compute_offer_count',
        required=False)


    reference = fields.Reference(selection = [('estate.property','Estate'),('sale.order','Sale')], string='Reference')

    def _compute_offer_count(self):
        offer_count = self.env['property.offer'].search_count([('property_type_id','=',self.id)])
        self.offer_count = offer_count
    def offer_action(self):
        return {
            'name': 'offer_action_view',
            'view_mode': 'tree,form',
            'res_model': 'property.offer',
            'domain': [('property_type_id','=',self.id)],
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'context': {}
        }

    def apply(self):
        # list = []
        # new = self.product_new_id.product_template_variant_value_ids
        # for rec in new:
        #     list.append(rec.name)
        # list = [rec.name for rec in self.product_new_id.product_template_variant_value_ids]
        # print(list)

        # new = [self.env['product.product'].search([])]
        # for i in new:
        #     if i.product_template_variant_value_ids != None:
        #         print(i)


        new = self.env['product.product'].search([])
        for rec in new:
            if rec.product_variant_count != 1:
                ids= rec.product_template_variant_value_ids
                list = []
                for i in ids:
                    list.append(i.name)
                print('--------------------->',rec.name,list)
    def sold(self):
        pass


    # def creating_rec(self):



