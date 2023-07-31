from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<h1> My Home <h1>"

@app.route("/test")
def hello_about():
    return"<h1> new <h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")