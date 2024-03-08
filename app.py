from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello")

@app.route("/symptoms", methods=["GET", "POST"])
def symptoms():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        return "Your name is "+first_name + last_name
    return render_template("symptom.html")

@app.route("/oils", methods=["GET", "POST"])
def oils():
    
    return render_template("oils.html")
