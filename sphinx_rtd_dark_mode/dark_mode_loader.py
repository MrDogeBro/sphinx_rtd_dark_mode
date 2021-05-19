from pathlib import Path


class DarkModeLoader:
    def __init__(self):
        self.config = None

    def configure(self, app, config):
        self.config = config

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
        pass

    def load_theme_switcher(self):
        if not self.config.html_js_files:
            self.config.html_js_files = [
                "dark_mode_js/theme_switcher.js",
            ]
        else:
            self.config.html_js_files.append("dark_mode_js/theme_switcher.js")

    def load_css(self):
        if "css_files" in self.config.html_context:
            self.config.html_context["css_files"].append("_static/dark_mode_css/general.css")
            self.config.html_context["css_files"].append("_static/dark_mode_css/dark.css")
            return

        if not self.config.html_css_files:
            self.config.html_css_files = [
                "dark_mode_css/general.css",
                "dark_mode_css/dark.css",
            ]
        else:
            self.config.html_css_files.append("dark_mode_css/general.css")
            self.config.html_css_files.append("dark_mode_css/dark.css")
