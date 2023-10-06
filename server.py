from http.server import HTTPServer
        
        
def start_server(host, port, views):
    server = HTTPServer((host, port), views)
    
    try:
        server.serve_forever()
        print("Server Started")
    except KeyboardInterrupt:
        pass
    server.server_close()
    print("Server Closed")