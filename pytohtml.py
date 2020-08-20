from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def index():
    headline = "Hello, Jack !"
    return render_template("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Good Bye !"
    return render_template("index.html", headline=headline)


app.run()
