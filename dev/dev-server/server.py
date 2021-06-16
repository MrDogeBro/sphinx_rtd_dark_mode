from colorama import Fore, Style
from datetime import datetime as dt, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from threading import Thread


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        custom_path = False

        if self.path == "/":
            self.path = "index.html"
        elif self.path == "/default/static/404.css":
            self.path = str(
                Path.joinpath(Path(__file__).resolve().parent, "static/404.css")
            )
            custom_path = True
        elif self.path == "/default/static/websocket.js":
            self.path = str(
                Path.joinpath(Path(__file__).resolve().parent, "static/websocket.js")
            )
            custom_path = True
        else:
            self.path = self.path[1:]
            if self.path.count("?") > 0:
                self.path = self.path[: self.path.rfind("?")]

        try:
            adjusted_path = None
            is_bytes = False

            if not custom_path:
                adjusted_path = self.output_path = Path.joinpath(
                    Path(__file__).resolve().parent, "../.dev-build/build", self.path
                )

            try:
                with open(adjusted_path if adjusted_path else self.path) as f:
                    requested_file = f.read()
            except UnicodeDecodeError:
                with open(adjusted_path if adjusted_path else self.path, "rb") as f:  # type: ignore[assignment]
                    # requested_file = f.read()
                    is_bytes = True

            self.send_response(200)
        except FileNotFoundError:
            with open(
                Path.joinpath(Path(__file__).resolve().parent, "static/404.html")
            ) as f:
                requested_file = f.read().replace("{REQUESTED_PAGE}", f"/{self.path}")

            self.send_response(404)

        if not is_bytes and self.path.endswith(".html"):
            if "<head>" in requested_file:
                requested_file = requested_file.replace(
                    "<head>",
                    f'<head><script src="default/static/websocket.js"></script>',
                )
            else:
                requested_file = requested_file.replace(
                    "<html>",
                    f'<html><head><script src="default/static/websocket.js"></script></head>',
                )

        self.end_headers()

        if is_bytes and isinstance(requested_file, bytes):
            self.wfile.write(requested_file)
            return

        self.wfile.write(bytes(requested_file, "utf-8"))

    def log_request(self, format, *args) -> None: # type: ignore[override]
        print(f"{Fore.GREEN}request{Fore.RESET} - {Style.DIM}{self.path} ({format}){Style.RESET_ALL}")
        return


class Server:
    def __init__(self):
        self.httpd = HTTPServer(("127.0.0.1", 5000), ServerHandler)
        self.thread = Thread(target=self.httpd.serve_forever)

    async def start(self) -> None:
        self.thread.start()

    async def stop(self) -> None:
        self.httpd.shutdown()
        self.thread.join()
