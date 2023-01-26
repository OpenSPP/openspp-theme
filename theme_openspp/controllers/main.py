from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.main import Home, ensure_db


class CustomSPPHome(Home):

    # def get_auth_signup_config(self):
    #     """Extends the get_auth_signup_config to add 'theme_openspp.show_login_user_pass' parameter"""
    #
    #     retval = super(CustomSPPHome, self).get_auth_signup_config()
    #     get_param = request.env["ir.config_parameter"].sudo().get_param
    #     retval.update(
    #         {"show_login_user_pass": get_param("theme_openspp.show_login_user_pass")}
    #     )
    #     return retval

    @http.route()
    def web_login(self, *args, **kw):
        ensure_db()
        response = super(CustomSPPHome, self).web_login(*args, **kw)
        get_param = request.env["ir.config_parameter"].sudo().get_param
        response.qcontext.update(
            {"show_login_user_pass": get_param("theme_openspp.show_login_user_pass")}
        )
        return response
