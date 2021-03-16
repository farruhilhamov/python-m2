from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "Hello im flask"

@app.route("/login/")
@app.route("/login/<name>")
def login(name):
    return "Hello im "+name+"!"

@app.route("/login2/")
@app.route("/login2/<name>")
def login2(name = None):
    return render_template("index.html",name=name)

if __name__ == "__main__":
    app.run()