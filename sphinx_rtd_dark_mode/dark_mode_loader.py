from pathlib import Path


class DarkModeLoader:
    def __init__(self):
        self.config = None
        self.app = None

    def configure(self, app, config):
        self.config = config
        self.app = app

        self.check_sphinx_theme()

        if not self.config.html_static_path:
            self.config.html_static_path = [
                str(Path.joinpath(Path(__file__).resolve().parent, "static"))
            ]
        else:
            self.config.html_static_path.append(
                str(Path.joinpath(Path(__file__).resolve().parent, "static"))
            )

        self.set_default_theme()
        self.load_theme_switcher()
        self.load_css()

    def check_sphinx_theme(self):
        if not self.config.html_theme == "sphinx_rtd_theme":
            self.config.html_theme = "sphinx_rtd_theme"

    def set_default_theme(self):
        default_theme = "dark"
        default_theme_enabled = "true"

        if not self.config.default_dark_mode:
            default_theme = "light"
            default_theme_enabled = "false"

        with open(
            Path.joinpath(Path(__file__).resolve().parent, "default_theme.js")
        ) as f:
            js_str = f.read()

        self.app.add_js_file(
            None,
            body=js_str.replace("{default_theme}", default_theme).replace(
                "{default_theme_enabled}", default_theme_enabled
            ),
        )

    def load_theme_switcher(self):
        if not self.config.html_js_files:
            self.config.html_js_files = [
                "dark_js/theme_switcher.js",
            ]
        else:
            self.config.html_js_files.append("dark_js/theme_switcher.js")

    def load_css(self):
        if "css_files" in self.config.html_context:
            self.config.html_context["css_files"].append(
                "_static/dark_css/theming.scss"
            )
            return

        if not self.config.html_css_files:
            self.config.html_css_files = [
                "dark_css/theming.scss",
            ]
        else:
            self.config.html_css_files.append("dark_css/theming.scss")
