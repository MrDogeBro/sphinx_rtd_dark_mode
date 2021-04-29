from pathlib import Path


class DarkModeLoader:
    def __init__(self):
        self.config = None

    def configure(self, app, config):
        self.config = config

        self.config.html_static_path = [
            str(Path.joinpath(Path(__file__).resolve().parent, "static"))
        ]

        if not self.config.default_dark_mode:
            self.load_default_light()
            return

        self.load_default_dark()

    def load_default_dark(self):
        self.config.html_js_files = [
            "dark_mode_js/default_dark.js",
            "dark_mode_js/theme_switcher.js",
        ]
        self.load_css()

    def load_default_light(self):
        self.config.html_js_files = [
            "dark_mode_js/default_light.js",
            "dark_mode_js/theme_switcher.js",
        ]
        self.load_css()

    def load_css(self):
        self.config.html_css_files = [
            "dark_mode_css/custom.css",
            "dark_mode_css/dark.css",
        ]


def setup(app):
    app.add_config_value("default_dark_mode", True, "html")

    app.connect("config-inited", DarkModeLoader().configure)

    return {
        "version": "1.0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
