
from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import  UserError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    _description = 'EstateProperty model for managing properties'
    _order = "id desc"


    property_type_id = fields.Many2one(
        comodel_name='property.type',
        string='Property Type',
        required=False)
    user_id = fields.Many2one(
        comodel_name='res.users',
        # default=lambda self:self.env.user,
        string='user',
        required=False)
    company_id = fields.Many2one(
        'res.company', string='Company', change_default=True,
        default=lambda self: self.env.company,
        required=False)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string='Currency')

    property_tag_ids = fields.Many2many(
        comodel_name='property.tag',
        string='Property_tag_ids')
    offer_ids = fields.One2many(
        comodel_name='property.offer',
        inverse_name='property_id',
        string='Offers',
        required=False)

    id = fields.Integer(
        string='Id',
        required=True)
    create_uid = fields.Integer(
        string='uid',
        required=False)
    create_date = fields.Date(
        string='Created date',
        required=False)
    write_uid = fields.Integer(
        string='Write uid',
        required=False)
    write_date = fields.Date(
        string='Write Date',
        required=False)
    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string="Description",
        required=False)
    ref = fields.Char(
        string='Reference No:',
        # default=lambda self: self.env['ir.sequence'].next_by_code('estate.property'),
        copy=False
    )
    postcode = fields.Char(
        string='Postcode',
        required=False)
    available_from = fields.Date(
        string='Available from',
        default=lambda self:date.today(),
        required=False)
    date_availability = fields.Date(
        string='Date_availability',
        default=lambda self: date.today() + relativedelta(months=+3),
        copy=False,
        required=False)
    # currency_id = fields.Many2one(
    #     comodel_name='res.currency',
    #     string='Currency',
    #     required=False)

    expected_price = fields.Monetary(
        'Expected Price',
        help="for adding expected price",
        required=True
    )
    selling_price = fields.Monetary(
        'Selling Price',
        readonly=True,
        copy=False
    )
    bedrooms = fields.Integer(
        string='Bedrooms',
        default=2,
        required=False)
    living_area = fields.Integer(
        string='Living Area',
        required=False)
    facades = fields.Integer(
        string='Facades',
        required=False)

    garage = fields.Boolean(
        string='Garage',
        required=False)
    garden = fields.Boolean(
        string='Garden',
        required=False)
    garden_area = fields.Integer(
        string='Garden Area',
        required=False)
    garden_orientation = fields.Selection(
        [('north','North'),('east','East'),('west','West'),('south','South')],
        string='Garden Orientation',
        required=False)
    active = fields.Boolean(
        default=True,
        string='Active',
        required=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'),
                   ('offer_accepted', 'Accept'),
                   ('offer_received','Received'),
                   ('sold','Sold'),
                   ('cancelled','Cancelled')],
        default='new',
        required=True, )
    buyer = fields.Char(
        string='Buyer',
        required=False,
        copy=False)
    sales_person = fields.Char(
        string='Sales Person',
        default= lambda self:self.env.user.name,
        required=False)
    total_area = fields.Float(
        string='Total Area',
        compute="_compute_total_area",
        required=False)
    best_price = fields.Float(
        string='Best price',
        compute='_compute_best_price',
        required=False)
    current_status = fields.Integer(
        string='Current status',
        default=0,
        required=False)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    image = fields.Image(
        string='Image'
            )

    total_valuation =fields.Monetary(
        'Total Valuation',
        compute='_compute_total_valuation',
        readonly=True,
        copy=False)






    @api.model
    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('estate.property')
        return super(EstateProperty, self).create(vals)

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        self.total_area = self.living_area+self.garden_area


    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            try:
                record.best_price = max(record.offer_ids.mapped('price'))
            except ValueError:
                record.best_price = 0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation='north'
        else:
            self.garden_area=0
            self.garden_orientation=None
    # @api.ondelete(at_uninstall=False)
    # def _ondelete_trigger_state(self):
    #     if self.state == 'new' or self.state == 'cancelled':
    #         pass
    #     else:
    #         raise UserError('cannot delete this data')
    def action_sold(self):
        if self.state != 'cancelled':
            self.state = 'sold'
        else:
            raise UserError('cancelled property cannot sold')
        return True
    def action_cancel(self):
        if self.state != 'sold':
            self.state = 'cancelled'
        else:
            raise UserError('cacelled properties cannot sold')
        return True
    _sql_constraints= [
        ('check_expected_price', 'CHECK(expected_price>0)','expected price should be greater than zero'),
        ('check_selling_price','CHECK(selling_price>0)','selling price should be greater than zero'),
        ('check_offer_price','CHECK(offer_ids.price>0)','offer price should be greater than zero'),
        ('check_tag_type','unique(property_tag_ids.name AND property_type_ids.name)','property tag and type should be unique')
    ]
    def action_demo(self):
        property_list = [{'name':'prop1','expected_price':50000},{'name':'prop2','expected_price':50000},{'name':'prop3','expected_price':50000}]
        print('exicuted ---------------------->')

        self.env['estate.property'].create(property_list)
        # print('-------->',self.env.user.name)
        # print('---->----->',self.env.user.id)
        # print('-------->',self.user_id)

    @api.depends('offer_ids.price')
    def _compute_total_valuation(self):
        for rec in self:
            self.total_valuation = sum(rec.offer_ids.mapped('price'))

    # @api.model
    # def default_get(self, fields):
    #    res = super(EstateProperty, self).default_get(fields)
    #    print('fields',fields)
    #    print('res',res)
    #    res['bedrooms']=32
    #    res['active'] = False
    #    print(self._context)
    #    return res


    def new_delete_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name':'delete_property',
            'res_model': 'delete.property.wizard',
            'view_mode': 'form',
            'context':{'default_property_id':self.id},
            'target':'new'

        }




