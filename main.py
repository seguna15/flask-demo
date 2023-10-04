from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/test")
def test():
    return "Hello, Test Route!"

@app.route("/welcome")
def welcome():
    return "Welcome!"
    
if __name__ == "__main__":
    print("server started")
    http_server = WSGIServer(('', 3000), app)
    http_server.serve_forever()