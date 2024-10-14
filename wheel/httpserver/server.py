from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import logging
from datetime import datetime

# ログの設定
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # 標準のログ出力をオーバーライド
        logging.info("%s - - [%s] %s" %
                     (self.client_address[0],
                      self.log_date_time_string(),
                      format%args))

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        try:
            with open(os.getcwd() + self.path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
                logging.info(f"200 GET {self.path}")
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))
            logging.warning(f"404 GET {self.path}")

    def do_HEAD(self):
        if self.path == '/':
            self.path = '/index.html'
        
        try:
            with open(os.path.join(os.getcwd(), self.path.lstrip('/')), 'rb'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                logging.info(f"200 HEAD {self.path}")
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))
            logging.warning(f"404 HEAD {self.path}")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f"Server started on port {port}")
    print(f"Server running on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server stopped")
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run()
