{
    "name": "OpenSPP Theme",
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp/openspp-theme",
    "category": "Theme",
    "version": "15.0.1.0.3",
    "depends": ["web"],
    "license": "AGPL-3",
    "development_status": "Beta",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "assets": {
        "web._assets_primary_variables": [
            "theme_openspp/static/src/scss/primary_variables.scss"
        ],
        "web.assets_backend": [
            "theme_openspp/static/src/scss/assets_backend.scss",
            "theme_openspp/static/src/scss/dynamic_dasbhoard.scss",
            "theme_openspp/static/src/js/basic_fields.js",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
