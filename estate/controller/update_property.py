from odoo import http
from odoo.http import request

class Updateproperty(http.Controller):

    @http.route('/update/', type='json', auth='user',methods=['POST'])
    def update_property_func(self, **rec):
        if rec['id']:
            vals ={
                'name':rec['name'],
                'expected_price':rec['expected_price']

            }
            proeprty = request.env['estate.property'].sudo().search([('id','=',rec['id'])])
            if property:
                proeprty.sudo().write(vals)

            args= {'message':'Success',}
            return args


