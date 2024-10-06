from extensions import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)
    team = db.Column(db.String(100), nullable = False, unique = True)
    mentor = db.Column(db.String(100), nullable = False)