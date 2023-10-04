from flask import Flask

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
    app.run(debug=True, port=8080)