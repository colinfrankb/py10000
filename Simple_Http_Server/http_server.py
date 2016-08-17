from http.server import BaseHTTPRequestHandler, HTTPServer


class CachedHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(dir(self.request))

        self.send_response(200)

        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(b'Welcome!')

        return

if __name__ == '__main__':
    print('http server is starting')
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, CachedHTTPRequestHandler)
    print('http server is running')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\rKeyboardInterrupt closing server.')
