from app import db

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hat = db.Column(db.String(50), nullable=True)
    shirt = db.Column(db.String(50), nullable=True)
    pants = db.Column(db.String(50), nullable=True)
    shoes = db.Column(db.String(50), nullable=True)
