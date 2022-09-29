from odoo import api, fields, models
import datetime


class DeleteProperty(models.TransientModel):
    _name = 'view.invoice.wizard'
    _description = 'show available invoices'

    partner_id = fields.Many2one(
       comodel_name='res.partner',
       string='customer',
       required=False)


    def show_invoice(self):
        new = self.env['sale.order'].search([('partner_id.id','=',self.partner_id.id)])
        print(new)
        for i in new:
            print(i.name,i.partner_id.name)
        # for i in new:
        #     if i.partner_id.name == self.partner_id.name:
        #         print(i.partner_id.name,i.name)

        # print(new)
        # for i in new:
        #     if i.partner_id == self.partner_id:
        #         print(i.partner_id,i.date_order)


