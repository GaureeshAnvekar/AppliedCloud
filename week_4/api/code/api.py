
from flask import Flask,render_template,jsonify
import json
import random
import os

app = Flask(__name__)
 
food = {"pizza" : 5, "chocolate": 4, "dosa" : 1, "croissant":2,"Amortentia":20 , "Polyjuice":12 , "Felix Felicis":43 , "Skele-Gro": 22,
"Wolfsbane":12, "Veritaserum":14 , "Jawbind": 20 , "Quodpot" : 25}

@app.route('/')
def landingpage():
    s = "Enjoy your meal!! :-)"
    return s

@app.route("/api/food",methods = ['GET'])
def food_dictionary():
    return jsonify({"food":food})

@app.route('/api/rand',methods= ['GET'])
def randres():
    res = key, val = random.choice(list(food.items()))
    return jsonify({"Dish: ": key, "Price ($): ": val})

if __name__ == "__main__":
    app.run('0.0.0.0', port = os.environ.get("API_PORT"),debug=True)


# Get random dictionary pair in dictionary
# Using random.choice() + list() + items()
    
# @app.route("/user")
# def user():
#     user_dict = get_user(request.args.get("id"))
#     return json.dumps(user_dict)
# @app.route("/birthdays")
# def birthdays():
# 	dates = {"Julian": 25, "Bob": 26, "Dan": 47, "Cornelius": 3}
# 	return render_template("birthdays.html", dates=dates)

# products = [{'name':'watch'},{'name':'pen'},{'name':'speaker'}]
# @app.route('/allproducts',method= ['get'])
# def getAllProducts():
#     return jsonify({"products":products})

    
# @app.route("/")
# def my_route():
#   content = {'thing':'some stuff',

#              'other':'more stuff'}

#   return render_template('food.html', **content)

# @app.route('/')
# def index():
#  return render_template('food.html')

# @app.route('/')
# def hello_geek():
#     return '<h1>Hello from Flask & Docker</h2>'

# @app.route('/')
# def get_current_user():
#     return '<h1>Hello from Flask & Dockeri</h2>'
    # return jsonify(<h1>
    #     username=g.user.username,
    #     email=g.user.email,
    #     id=g.user.id </h2>
    # )


