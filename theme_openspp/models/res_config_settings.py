from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_login_user_pass = fields.Boolean(
        string="Show Username and Password in Login Interface",
        config_parameter="theme_openspp.show_login_user_pass",
        default=True,
    )
