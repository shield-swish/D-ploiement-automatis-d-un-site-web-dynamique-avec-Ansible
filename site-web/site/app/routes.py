from flask import render_template, request
from app import app, db
from app.models import Message

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        nom = request.form.get("name")
        email = request.form.get("email")
        contenu = request.form.get("message")
        nouveau = Message(nom=nom, email=email, contenu=contenu)
        db.session.add(nouveau)
        db.session.commit()
        message = "Merci ! Votre message a été enregistré."
    return render_template("index.html", message=message)
