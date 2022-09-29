from odoo import http
from odoo.http import request
@http.route('/web/session/authenticate', type='json', auth="none")
def authenticate(self, db, login, password, base_location=None):
    request.session.authenticate(db, login, password)
    return request.env['ir.http'].session_info()
