import http.server, os, sys
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        p=self.path.split('?')[0]
        if not os.path.exists('.'+p) or p=='/': self.path='/index.html'
        super().do_GET()
http.server.test(H, port=int(sys.argv[1]) if len(sys.argv)>1 else 8080)
