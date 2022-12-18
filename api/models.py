from api import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingr= db.Column(db.Text, nullable=False)
    inst= db.Column(db.Text, nullable=False)
    rate = db.Column(db.Integer, nullable=False, default=0)
    star = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, ingr, inst,  star, rate):
        self.name = name
        self.ingr = ingr
        self.inst = inst
        self.star = star
        self.rate = rate
