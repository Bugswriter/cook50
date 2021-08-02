from cookpkg import app
from cookpkg.crud import *
from flask import request

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
