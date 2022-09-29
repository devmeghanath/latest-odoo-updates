from odoo import http
from odoo.http import request
@http.route('/web/session/destroy', type='json', auth="user")
def destroy(self):
    request.session.logout()