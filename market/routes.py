from market import app , db  #bcrypt
from market.models import User , Car,Comment,UserSchema ,user_schema ,CommentSchema, comment_schema , comments_schema , CarSchema , car_schema , cars_schema 
from flask import render_template , request , jsonify
import market.models
#from werkzeug.security import generate_password_hash, check_password_hash


# Add new user infos -------------------------------
@app.route("/SignUp" , methods=['POST' , 'GET'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    region = request.json['region']
    new_user = User(username , email , password , region)
    db.session.add(new_user)
    db.session.commit()
    return "True"

#add new car announcment -----------------------------
@app.route("/announces/add", methods=['POST' , 'GET'])
def add_car():
    name = request.json['name']
    selling_price = request.json['selling_price']
    km_driven = request.json['km_driven']
    fuel =  request.json['fuel']
    year = request.json['year']
    seller_type =  request.json['seller_type']
    transmission = request.json['transmission']
    mileage = request.json['mileage']
    engine = request.json['engine']
    max_power = request.json['max_power']
    seats = request.json['seats']
    owner = request.json['owner']
    region = request.json['region']

    new_car = Car(name,selling_price,km_driven ,fuel, year,
    seller_type,transmission,mileage,engine,
    max_power,seats,owner , region)

    db.session.add(new_car)
    db.session.commit()
    return "True"

# Show available cars ---------------------------
@app.route("/announces" , methods=['GET' , 'POST'])
def show_cars():
    
    all_cars = Car.query.all()
    result = cars_schema.dump(all_cars)
    return jsonify(result)

#Show announce ------------------------------
@app.route("/announces/<id>" , methods=['GET' , 'POST'])
def show_car(id):
    car = Car.query.get(id)
    return car_schema.jsonify(car)

# Show comments ---------------------------
@app.route("/announces/<id>/comments" , methods=['GET' , 'POST'])
def show_comments(id):
    announce_comments = Comment.query.filter_by(car_id=id)
    result = comments_schema.dump(announce_comments)
    return jsonify(result)

# Add comment to an announce ------------------
@app.route("/announces/<id>/add" , methods=['POST','GET'])
def add_comment(id):
    content = request.json['content']
    new_comment = Comment(content , id)
    db.session.add(new_comment) 
    db.session.commit()
    return "True"


#login into the account----------------------
@app.route("/signin" , methods=['POST'])
def sign():
    username = request.json['username']
    password = request.json['password']
    current_user = User.query.filter_by(username=username).first()
    if current_user.password == password:
        global accessed 
        accessed = True
        return "True"
    else : 
        return "False"

#show the profile of the user ------------------
@app.route("/profile/<id>" , methods=['POST' , 'GET'])
def show_profile(id):
    user_viewed = User.query.filter_by(id=id).first()
    result = user_schema.dump(user_viewed)
    return jsonify(result)

#search for cars search bar -------------------------
# @app.route("/search" , methods=['POST' , 'GET'])
# def car_search():
#     name = request.json['name']
#     #min_price = request.json['min_price']
#     #max_price = request.json['max_price']
#     year = request.json['year']
#     region = request.json['region']
#     fuel = request.json['fuel']
#     wanted_cars = Car.query.filter_by(name=name or year=year or region=region or fuel=fuel)
#     result = cars_schema.dump(wanted_cars)
#     return jsonify(result)
    
