import server
from src.views import UrlShortHost
from src.views import shorten_url
from config import HOST, PORT
import sys


if __name__ == '__main__':
    if sys.argv[1] == 'startserver':
        server.start_server(HOST, PORT, UrlShortHost)
    elif sys.argv[1] == 'shorten':
        shorten_url()
    else:
        print("Command not found. Try the following command: ")
        print("python main.py startserver ------- [Run this command to start server]")
        print("python main.py shorten ------- [Start CLI to shorten the URL]")