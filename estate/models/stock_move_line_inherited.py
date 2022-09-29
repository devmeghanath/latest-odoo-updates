from odoo import api, fields, models


class StockmovelineInherit(models.Model):

    _inherit = 'stock.move'




    restrict_lot_id = fields.Many2one(
        comodel_name='stock.production.lot',
        string='restrict lot id',
        required=False)
    

    sample = fields.Char(
        string='Sample',
        required=False)
    new_field = fields.Char(
        string='New_field',
        required=False)








    # @api.model
    # def _prepare_procurement_values(self):
    #     vals = super()._prepare_procurement_values()
    #     vals["new_lot_id"] = self.new_lot_id.id
    #     return vals

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super()._prepare_move_line_vals(
            quantity=quantity, reserved_quant=reserved_quant
        )
        if self.restrict_lot_id:

            vals["lot_id"] = self.restrict_lot_id.id
        return vals



class StockRuleInh(models.Model):
    _inherit = "stock.rule"
    #
    # def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
    #     res = super(StockRuleInh, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
    #     res['sample'] = values.get('sample','no value')
    #     return res

    def _get_custom_move_fields(self):
        fields = super()._get_custom_move_fields()
        fields += ["restrict_lot_id","sample","new_field"]
        return fields

class StockPicking(models.Model):
    _inherit = "stock.picking"

    sample = fields.Char(
        string='Sample',
        required=False)
    new_field = fields.Char(
        string='New_feild',
        required=False)



    def do_print_picking(self,):
        res =super(StockPicking, self).do_print_picking()
        new = self.env['stock.move'].search([('origin','=',self.origin)])
        for i in new:
            print('------------------------------------->',i.sample)
            print('------------------------------------->',i.restrict_lot_id)
            print('------------------------------------->',i.origin)








    #
    # def create(self,vals):
    #     res = super(StockmovelineInherit, self).create(vals)
    #     if self.sample:
    #         print('------------------------------------------>',self.sample)
    #     else:('--------------------------> no values available')
    #     return res
    #
    #
    #

    # def create(self,vals):
    #
    #
    #     vals={
    #         'lot_id'
    #     }
    #     res = super(StockmovelineInherit, self).create(vals)
    #
    #     return res
    # #
    # def _update_reserved_quantity(self, need, available_quantity, location_id, lot_id=None, package_id=None,
    #                               owner_id=None, strict=True):
    #     lot_id = '123'
    #
    #
    #
    #     return super(StockmovelineInherit, self)._update_reserved_quantity()



    #
    # lot_id = fields.Many2one(
    #     'stock.production.lot', 'Lot/Serial Number',
    #     related='move_id.sale_line_id.lot_id',
    #     domain="[('product_id', '=', product_id), ('company_id', '=', company_id)]", check_company=True)
    #




    #important code for writhing in active ids
    # if self.order_lines_ids:
    #     for i in self.order_lines_ids:
    #         vals = {'product_id': i.product_id.id,
    #                 'name': i.product_description,
    #                 'product_uom_qty': i.product_quantity,
    #                 'price_unit': i.price_unit,
    #                 'tax_id': i.tax_id,
    #                 }
    #         self.env['sale.order'].browse(self._context.get("active_ids")).update({'order_line': [(0, 0, vals)]})