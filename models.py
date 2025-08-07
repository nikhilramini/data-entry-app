from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(100), nullable=False)
    hometown = db.Column(db.String(100), nullable=True)
