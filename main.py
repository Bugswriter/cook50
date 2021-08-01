import sqlite3
from flask import Flask, request

app = Flask(__name__)

def crud_add_recipe(data):
    conn = sqlite3.connect('cook50.db')
    c = conn.cursor()
    keys = "(name, rating, difficulty, type, prep_time, main_ingredients, recipe_link)" 
    values = "('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(data['n'], data['r'], data['d'], data['rt'], data['pt'], data['mi'], data['rl'])
    sql = "INSERT INTO recipe {} VALUES {}".format(keys, values)
    try:
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured:" , e.args[0])
        return False

    conn.close()
    return True


@app.route('/')
def home():
    return "Welcome to the homepage\n"

@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    data = {
        "n": request.form["n"],
        "r": request.form["r"],
        "d": request.form["d"],
        "rt": request.form["rt"],
        "pt": request.form["pt"],
        "mi": request.form["mi"],
        "rl": request.form["rl"]
    }
    if crud_add_recipe(data):
        return "Adding successfully\n"
    else:
        return "Error"
    
if __name__=="__main__":
    app.run(debug=True)
