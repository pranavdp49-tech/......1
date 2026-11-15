import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path in ('/api/pipeline/data', '/api/telemetry'):
            telemetry_path = os.path.join(DIRECTORY, "telemetry_250m.json")
            if os.path.exists(telemetry_path):
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                with open(telemetry_path, 'rb') as f:
                    self.wfile.write(f.read())
                return
        super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"=======================================================")
        print(f" NASA Field Farm - Agro-Ecological Decision Portal")
        print(f" Server running at: {url}")
        print(f" Press Ctrl+C to stop the server")
        print(f"=======================================================")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down.")
            httpd.shutdown()

if __name__ == '__main__':
    run()
