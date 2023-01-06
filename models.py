from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Employee(db.Model):
    __tablename__ = 'results'

    name = db.Column(db.String(30),primary_key = True)
    age = db.Column(db.Integer())

    def __init__(self, name,age):
        self.name = name
        self.age  = age
        
    def __repr__(self):
        return '<id {self.}>'.format(self.name)


