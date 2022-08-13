{
    "name": "OpenSPP Theme",
    "author": "OpenSPP.org",
    "website": "https://openspp.org/",
    "category": "Theme",
    "version": "15.0.0.0.1",
    "depends": ["base"],
    "license": "AGPL-3",
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
