from odoo import api, fields, models



class NewModule(models.Model):

    _inherit = 'sale.order'


    # def _prepare_procurement_values(self, group_id=False):
    #     """ Prepare specific key for moves or other components that will be created from a stock rule
    #     comming from a sale order line. This method could be override in order to add other custom key that could
    #     be used in move/po creation.
    #     """
    #     for line in self.order_line:
    #         print(line)
    #     return {}
    #



    property_id = fields.Many2one(
        comodel_name='estate.property',
        string='Proeprty_id',
        required=False)


    #
    def action_demo(self):
        pass
        # value =self.order_line.lot_id.id
        # self.env['stock.move.line'].write({'lot_id': value})
        # print('exicuted---------------------------------------->')
        # print(value)
        # ls = [i for i in range(10)]
        # val={'ls':ls}
        # val.update({'ls':[]})
        # return val
        # self.env['estate.property'].create({'name':'bug testing','expected_price':500000})
        # vals = self.env['estate.property'].search([('name' ,'=', 'bug testing'),('expected_price', '=', 500000)])
        # for i in vals:
        #     v= self.env['estate.property'].browse(i.id)
        #     v.write({'name':'bug','expected_price':50})
        #
    
    
class NewModule(models.Model):

    _inherit = 'product.template'
    
    
    
    is_rendered = fields.Boolean(
        string='Is rended',
        required=False)



