from http.server import SimpleHTTPRequestHandler
import socketserver

# Define the request handler
class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Respond to GET requrests
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello world!")

# Define the serve and port
PORT = 8080

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()    

