from odoo import api, fields, models
from odoo import Command
import datetime


class BaseModule(models.Model):
    _name = 'sample.module'
    _rec_name = 'partner_id'



    partner_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('city','=','Fremont')],
        string='customer',
        required=False)
    partner = fields.Char(
        string='Partner', 
        required=False)






    def action_invoice(self):
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()

        self.env['account.move'].create({
            'partner_id' : self.partner_id.id,
            'move_type' : 'out_invoice',
            'journal_id' : journal.id,
            'invoice_date' : datetime.date.today(),
            'invoice_line_ids' : [
                Command.create({'name':'prdouct1','quantity':2,'price_unit':7}),
                Command.create({'name':'prdouct2','quantity':2,'price_unit':10}),

            ]
        })








