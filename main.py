import sqlite3
from flask import Flask, request

app = Flask(__name__)

#=================
# CRUD Functions #
#=================

# CRUD funciton for adding new recipe
#==================================================
def crud_add_recipe(data):
    conn = sqlite3.connect('cook50.db')
    c = conn.cursor()
    values = "('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(data['n'], data['r'], data['d'], data['rt'], data['pt'], data['mi'], data['rl'])
    sql = "INSERT INTO recipe VALUES {}".format(values)
    try:
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: " , e.args[0])
        
    conn.close()

# CRUD function for getting recipes
#==================================================
def crud_get_recipes(offset):
    conn = sqlite3.connect('cook50.db')
    c = conn.cursor()
    data = []
    for row in c.execute("SELECT rowid, * FROM recipe LIMIT 10 OFFSET {}".format(offset)):
        data.append(list(row))

    return data

# CRUD function for deleting recipe
#==================================================
def crud_delete_recipe(rowid):
    conn = sqlite3.connect('cook50.db')
    c = conn.cursor()
    try:
        sql = "DELETE FROM recipe WHERE rowid={}".format(rowid)
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])


#==================
# Route Functions #
#==================

# Homepage route
#==================================================
@app.route('/')
def home():
    return "Welcome to the homepage\n"


# Get recipe data
#==================================================
@app.route("/recipes", methods=["GET"])
def recipes():
    offset = 0
    if request.args.get('page'):
        page = int(request.args.get('page'))
        offset = 10 * (page - 1)

    data = crud_get_recipes(offset)
    for row in data:
        print(row)
    return "We got data\n"

# Add new recipe
#==================================================
@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    if request.method == "POST":
        data = {
            "n": request.form["n"],
            "r": request.form["r"],
            "d": request.form["d"],
            "rt": request.form["rt"],
            "pt": request.form["pt"],
            "mi": request.form["mi"],
            "rl": request.form["rl"]
        }
        crud_add_recipe(data)
        return "Redirect to /recipes\n"

    return "Form to add recipe\n"


# Delete recipe
#==================================================
@app.route("/delete_recipe", methods=["GET"])
def delete_recipe():
    if request.args.get("id"):
        rowid = int(request.args.get("id"))
        crud_delete_recipe(rowid)
        return "1"

    return "0" 
    

#=================
# Main Functions #
#=================
if __name__=="__main__":
    app.run(debug=True)
