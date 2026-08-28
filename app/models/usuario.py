<<<<<<< HEAD
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), 
                         index=True, 
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(64), 
                        index=True, 
                        unique=True,
                        nullable=False)
    password_hash = db.Column(db.String(256))
=======
from  app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, 
                   primary_key=True)
    username = db.Column(db.String(64), 
                         index=True, 
                         unique=True, 
                         nullable=False)
    email = db.Column(db.String(64), 
                      index=True, 
                      unique=True, 
                      nullable=False)
    password_hash = db.Column(db.String(256))
>>>>>>> b25a6837451576e384a6d86b0372eb1612f8723f
