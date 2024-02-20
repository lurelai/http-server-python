from http.server import HTTPServer, BaseHTTPRequestHandler

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello World", "utf-8"))

if __name__ == "__main__":
    app = HTTPServer(("localhost", 8080), App)
    app.serve_forever()
    pass

