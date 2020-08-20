from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    names = ["Alex", "Bob", "Charlie", "Don"]
    return render_template("list.html", names=names)


app.run()
