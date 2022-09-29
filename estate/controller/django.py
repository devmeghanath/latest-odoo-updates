from odoo import http
import json
from odoo.http import request,Response
class EstateProperty(http.Controller):
    @http.route('/estate/',auth='user',methods = ['GET'])
    def estate_property(self, **kw):
        headers_json = {'Content-Type': 'application/json',}
        data = [{'name':l.name,'type':l.property_type_id.name,'bedrooms':l.bedrooms} for l in request.env['estate.property'].sudo().search([]) ]
        result = {
            'data': data,
            'errors': {},
            'meta': {}
        }
        return Response(json.dumps(result), headers=headers_json)

