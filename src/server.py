from http.server import HTTPServer, BaseHTTPRequestHandler

def read_html_content(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()
    return html_content

html_file_path = 'subfolder/basic_page.html'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(read_html_content(html_file_path).encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
    
#fix: this is a temporary solution for running this website locally