from odoo import http
from odoo.http import request
class EstateProperty(http.Controller):
    @http.route('/create/', type='json',auth='user',methods=['POST'])
    def estate_property(self, **rec):
         if rec['name'] and rec['expected_price']:
             vals = {
                 'name':rec['name'],
                 'expected_price':rec['expected_price']
             }
             new_property = request.env['estate.property'].sudo().create(vals)
             args = {'success':True,'message':'Success','ID':new_property.id}
             return  args




