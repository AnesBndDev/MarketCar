from market import db , mar  #bcrypt
from flask_login import UserMixin

class User(db.Model): #creating user infos table------------------------------
    id= db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=20),nullable=False, unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password = db.Column(db.String(length=60), nullable=False, default=5000)
    region = db.Column(db.String(length=20),nullable=False, unique=False)
    comment_owner= db.relationship('Comment')
    #rating = db.Column(db.Integer(), nullable=True , unique=False  , default=0)
    def __init__(self, username , email , password , region):
        self.username = username
        self.email = email
        self.password = password
        self.region = region
    
#  Schema
class UserSchema(mar.Schema):
  class Meta:
    fields = ('id', 'username' , 'email','password' , 'region')

# Init schema
user_schema = UserSchema()


class Car(db.Model): #car infos------------------------------------------------
    id= db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    selling_price = db.Column(db.Integer(), nullable=False)
    km_driven = db.Column(db.Integer(), nullable=False)
    fuel = db.Column(db.String(length=70), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    seller_type = db.Column(db.String(length=40), nullable=False)
    transmission = db.Column(db.String(length=50), nullable=False)
    mileage = db.Column(db.Integer(), nullable=False)
    engine = db.Column(db.Integer(), nullable=False)
    max_power = db.Column(db.Integer(), nullable=False)
    seats = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.String(length=30), nullable=False)#how many driver drived it ---------------
    region = db.Column(db.String(length=30), nullable=False)
    owner_id = db.Column(db.Integer(),db.ForeignKey("user.id"))
    def __init__(self , name,selling_price,km_driven ,fuel, year,
    seller_type,transmission,mileage,engine,
    max_power,seats,owner,region):
        self.name = name 
        self.selling_price = selling_price
        self.km_driven = km_driven 
        self.fuel = fuel
        self.year = year 
        self.seller_type = seller_type
        self.transmission = transmission
        self.mileage = mileage
        self.engine = engine
        self.max_power = max_power
        self.seats = seats
        self.owner = owner
        self.region = region
    

# Product Schema
class CarSchema(mar.Schema):
  class Meta:
    fields = ('id', 'name', 'selling_price', 'km_driven', 'fuel' , 'year' , 
    'seller_type' , 'transmission' , 'mileage' , 'engine' , 'max_power' , 
    'seats' , 'owner' , 'owner_id')

# Init schema
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

class Comment(db.Model): #commenets for an announce ---------------------------------
    id = db.Column(db.Integer() , primary_key=True)
    content = db.Column(db.String(length=100),nullable=False )
    car_id = db.Column(db.Integer() , db.ForeignKey('car.id'))
    user_id = db.Column(db.Integer() , db.ForeignKey('user.id'))
    def __init__(self , content , car_id):
        self.content = content
        self.car_id = car_id 
        #self.user_id = user_id
class CommentSchema(mar.Schema):
    class Meta:
        fields = ('id' , 'content' , 'car_id' , 'user_id')

#init schema--
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
    

# class Favor(db.Model):
#     id = db.Column(db.Integer() , primary_key=True)
#     car_id = db.Column(db.Integer() , db.ForeignKey('car.id'))
#     user_id = db.Column(db.Integer() , db.ForeignKey('user.id'))
    

# class Note(db.Model): #---------------
#     id = db.Column(db.Integer() , primary_key=True)
#     content = db.Column(db.Integer(),nullable=False)
#     user_id = db.Column(db.Integer() , db.ForeignKey('user.id'))




