from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homeforms.html")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    name = request.form.get("name")
    title = f"Hello {name}"
    return render_template("hello.html", name=name, title=title)


app.run()
