import sqlite3
from flask import Flask, request

app = Flask(__name__)

def crud_add_recipe(name, rating, difficulty, recipe_type, prep_time, main_ingredients, recipe_link):
    conn = sqlite3.connect('cook50.db')
    cur = con.cursor()
    print("I am in a crud function")
    print(name)


@app.route('/')
def home():
    return "Welcome to the homepage\n"

@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    if request.method != "POST":
        return "Wrong Method"

    data = {}
    data["name"] = request.form["name"]
    data["rating"] = request.form["rating"]
    data["difficulty"] = request.form["difficulty"]
    data["recipe_type"] = request.form["recipe_type"]
    data["prep_time"] = request.form["prep_time"]
    data["main_ingredients"] = request.form["main_ingredients"]
    data["recipe_link"] = request.form["recipe_link"]
    crud_add_recipe(**data)

    return "Testing"
    

if __name__=="__main__":
    app.run(debug=True)
