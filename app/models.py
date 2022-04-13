from app import db


class Area(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    coord = db.Column(db.String(32))
    area_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(50000))
