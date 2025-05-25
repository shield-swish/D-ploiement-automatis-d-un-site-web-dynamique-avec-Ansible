from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
