# # -*- coding: utf-8 -*-
{
    'name': "OpenSPP Theme",
    'author': "OpenSPP.org",
    'website': "https://openspp.org/",
    'category': 'Theme',
    'version': '0.3',
    "depends": ["base"],
    "license": "OPL-1",
    "assets": {
        "web._assets_primary_variables": [
            "theme_openspp/static/src/scss/primary_variables.scss"

        ],
        "web.assets_backend": [
            "theme_openspp/static/src/scss/assets_backend.scss",
            "theme_openspp/static/src/scss/dynamic_dasbhoard.scss",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
