from cookpkg import app
from cookpkg.crud import *
from flask import request, render_template, redirect, url_for

#==================
# Route Functions #
#==================

# Homepage route
#==================================================
@app.route('/')
def home():
    return render_template("home.html")


# Get recipe data
#==================================================
@app.route("/recipes", methods=["GET"])
def recipes():
    offset = 0
    if request.args.get('page'):
        page = int(request.args.get('page'))
        offset = 10 * (page - 1)

    data = crud_get_recipes(offset)
    return render_template("recipe_list.html", data=data)


# Add new recipe
#==================================================
@app.route("/add_recipe", methods=["GET", "POST"])
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
        return redirect(url_for('recipes'))

    return render_template("add_recipe.html")


# Delete recipe
#==================================================
@app.route("/delete_recipe", methods=["GET"])
def delete_recipe():
    if request.args.get("id"):
        rowid = int(request.args.get("id"))
        crud_delete_recipe(rowid)
        return redirect(url_for('recipes'))

    abort(500)
