# Python Program to Get IP Address
import socket
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return 'Hello World! HostName {} ipaddress{}\n'.format(hostname,IPAddr)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



