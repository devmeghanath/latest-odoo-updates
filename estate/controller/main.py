from odoo import http
import json
from odoo.http import request,Response
class EstateProperty(http.Controller):
    @http.route('/type/',auth='user',methods=['GET'])
    def estate_property(self, **kw):
         data = [{'name':l.name} for l in request.env['property.type'].sudo().search([])]
         new = {'status':200,'data':data,'message':'Success'}

         return  new

