from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager





         

    

class Flavor(db.Model):
    __tablename__="flavor"

    id=db.Column(db.Integer,primary_key=True)
    pizza_id=db.Column(db.Integer)
    name=db.Column(db.String)
    price=db.Column(db.Integer,unique=True)
    pizza = db.relationship('Pizza', backref = "flavor", lazy = 'dynamic')
   
    

    def save_flavor (self):
        db.session.add(self)
        db.session.commit()


class Size (db.Model):

    __tablename__ = 'size'

    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String)
    price = db.Column(db.Integer,unique=True)
    pizza = db.relationship('Pizza', backref = "size", lazy = 'dynamic')
    


    def save_size(self):
        db.session.add(self)
        db.session.commit()


class Toppings(db.Model) :

    __tablename__ = 'toppings'

    id = db.Column(db.Integer, primary_key = True)
    toppings = db.Column(db.String)
    price =db.Column(db.Integer,unique=True)
    pizza = db.relationship('Pizza', backref = "toppings", lazy = 'dynamic')
    
    def save_toppings(self):
        db.session.add(self)
        db.session.commit()


class Pizza(db.Model):
    '''
    Pizza ito define Pizza objects
    '''

    __tablename__='pizza'
     
    id=db.Column(db.Integer,primary_key=True)
    size_price=db.Column(db.Integer,db.ForeignKey('size.price'))
    flavor_price =db.Column(db.Integer,db.ForeignKey('flavor.price'))
    toppings_price=db.Column(db.Integer,db.ForeignKey('toppings.price'))
    price=db.Column(db.Integer)
    



    def save_pizza(self):
        db.session.add(self)
        db.session.commit()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255)) 

    @login_manager.user_loader
    def load_user (id):
        return User.query.get(int(id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


