from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/":
            self.path = "index.html"
        elif self.path == "/default/static/404.css":
            self.path = str(
                Path.joinpath(Path(__file__).resolve().parent, "static/404.css")
            )
        elif self.path == "/default/static/socket.js":
            self.path = str(
                Path.joinpath(Path(__file__).resolve().parent, "static/socket.js")
            )
        else:
            self.path = self.path[1:]

        try:
            with open(self.path) as f:
                requested_file = f.read()

            self.send_response(200)
        except FileNotFoundError:
            with open(
                Path.joinpath(Path(__file__).resolve().parent, "static/404.html")
            ) as f:
                requested_file = f.read().replace("{REQUESTED_PAGE}", f"/{self.path}")

            self.send_response(404)

        if "<head>" in requested_file:
            requested_file = requested_file.replace(
                "<head>", f'<head><script src="default/static/websocket.js"></script>'
            )
        else:
            requested_file = requested_file.replace(
                "<html>",
                f'<html><head><script src="default/static/websocket.js"></script></head>',
            )

        self.end_headers()
        self.wfile.write(bytes(requested_file, "utf-8"))


class Server:
    async def start(self):
        httpd = HTTPServer(("127.0.0.1", 5000), ServerHandler)
        httpd.serve_forever()
