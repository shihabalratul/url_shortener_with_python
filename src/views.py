from http.server import BaseHTTPRequestHandler
from . import db_con
from .generate_url import generate_url
from config import HOST, PORT
import sys, os

class UrlShortHost(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        db = db_con.database_connection()
        if db is not None:
            cur = db.cursor()
            cur.execute(f"SELECT * FROM urls WHERE short_url = '{url}'")
            
            data = cur.fetchone()
            
            if data is None:
                self.send_response(404)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("<html><body><h1>Link not found</h1></body></html>", "utf-8"))    
            else:
                self.send_response(301)
                self.send_header('Location', data[1])
                self.end_headers()    
            db.close()
            
        else:
            print("Database not connected")
        

def shorten_url():
    while True:
        url = input("Enter a URL to shorten: ")
        
        path = generate_url()
        short_url = f"http://{HOST}:{PORT}/{path}"
        
        db = db_con.database_connection()
        
        if db:
            curr = db.cursor()
            
            curr.execute(f"INSERT INTO urls VALUES ('{path}','{url}')")
            db.commit()
            
            db.close()
            
        print(short_url)
            