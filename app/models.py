"""Generic data storage.  Foreign keys avoided"""
from app import db


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    url = db.Column(db.String(64))


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, index=True)
    key_1 = db.Column(db.String(256))
    key_2 = db.Column(db.String(256))
    key_3 = db.Column(db.String(256))
    key_4 = db.Column(db.String(256))
    key_5 = db.Column(db.String(256))
    key_6 = db.Column(db.String(256))
    key_7 = db.Column(db.String(256))
    key_8 = db.Column(db.String(256))
    name = db.Column(db.String(256))
    value = db.Column(db.String(256)) 
