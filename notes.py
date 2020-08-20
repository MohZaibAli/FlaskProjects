from flask import Flask, render_template, session, request
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/session2", methods=["GET", "POST"])
def knots2():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html", notes=session["notes"])


notes = []


@app.route("/", methods=["GET", "POST"])
def knots():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("notes.html", notes=notes)


@app.route("/session1", methods=["GET", "POST"])
def knots1():
    session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html", notes=session["notes"])


app.run()
