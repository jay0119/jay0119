from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<h1>HELLO, WORLD My name jayprasad<h1>"

@app.route("/test")
def test():
    a = 7+5
    return "this is my function to run app {}". format(a)

@app.route("/login")
def login():
    return "log in"

@app.route("/test1/test1")
def test1 ():
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")