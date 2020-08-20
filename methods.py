from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homeforms.html")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return f"Please Submit The Form First."
    else:
        name = request.form.get("name")
        title = f"Hello {name}"
        return render_template("hello.html", name=name, title=title)


app.run()
