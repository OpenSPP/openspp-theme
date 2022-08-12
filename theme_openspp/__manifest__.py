# # -*- coding: utf-8 -*-
{
    'name': "OpenSPP Theme",
    'author': "Newlogic",
    'website': "https://newlogic.com/",
    'category': 'Theme',
    'version': '0.3',
    "depends": ["base"],
    "installable": True,
    "license": "OPL-1",
    "assets": {
        "web._assets_primary_variables": [
            "theme_openspp/static/src/scss/primary_variables.scss"

        ],
        "web.assets_backend": [
            "theme_openspp/static/src/scss/assets_backend.scss",
            "theme_openspp/static/src/scss/dynamic_dasbhoard.scss",
        ],
    }
}
