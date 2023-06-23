from http.server import HTTPServer, BaseHTTPRequestHandler
import json
HOST='192.168.1.105'
PORT = 8000

lst=[]
class Hossein(BaseHTTPRequestHandler):
    # def res(self):
    #     return json.dumps(lst)
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(lst).encode('utf-8'))

    # def do_POST(self):
    #     content_len = int(self.headers.get('Content-Length'))
    #     post_body = self.rfile.read(content_len)
    #     post_body1=json.loads(post_body)
    #     lst.append(post_body1)
    #     self.send_response(200)
    #     self.send_header('Content-Type', 'application/json')
    #     self.end_headers()
    #     self.wfile.write('finish'.encode('uft-8'))
        
    
server=HTTPServer((HOST,PORT),Hossein)
print('on')
server.serve_forever()
server.server_close()