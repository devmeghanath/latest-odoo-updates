from odoo import api, fields, models
from odoo import Command


class EstateProperty(models.Model):

    _inherit = 'estate.property'


    def action_sold(self):


            journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
            self.env["account.move"].create(

                {
                    'partner_id':self.offer_ids.partner_id.id,
                    'move_type':'out_invoice',
                    'journal_id':journal.id,

                    'invoice_line_ids': [
                        Command.create({'name':self.name,  'quantity': 1,'price_unit':self.selling_price}),
                        Command.create({'name':'commision',  'quantity': 1,'price_unit':-(self.selling_price*(6/100))}),
                        Command.create({'name':'administrative fee',  'quantity': 1,'price_unit':-(100)}),

                    ],


                })
            return super().action_sold()

