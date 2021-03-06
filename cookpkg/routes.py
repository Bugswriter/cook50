#==================
# Route Functions #
#==================
from cookpkg import app
from cookpkg.crud import *
from flask import request, render_template, redirect, url_for, flash, make_response

# Homepage route
#==================================================
@app.route('/')
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.cookies.get("user_id"):
        return redirect(url_for("recipes"))

    if request.method == "POST":
        data = {
            "u": request.form["u"],
            "e": request.form["e"],
            "p": request.form["p"]
        }
        register_user(data)
        return redirect(url_for('login'))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.cookies.get("user_id"):
        return redirect(url_for('recipes'))

    if request.method == "POST":
       username = request.form["u"]
       password = request.form["p"]
       user = check_login_cred(username, password)
       if user:
           res = make_response(redirect(url_for('recipes')))
           res.set_cookie("user_id", str(user[0]))
           return res

    return render_template("login.html")


@app.route("/logout")
def logout():
    res = make_response(redirect(url_for("home")))
    if request.cookies.get("user_id"):
        res.delete_cookie("user_id")

    return res


# Get recipe data
#==================================================
@app.route("/recipes", methods=["GET"])
def recipes():
    if not request.cookies.get("user_id"):
        return redirect(url_for('login'))

    uid = request.cookies.get("user_id")
    data = crud_get_recipes(uid)
    return render_template("recipe_list.html", data=data)


# Add new recipe
#==================================================
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if not request.cookies.get("user_id"):
        return redirect(url_for('login'))

    if request.method == "POST":
        data = {
            "ui": request.cookies.get("user_id"),
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
    if not request.cookies.get("user_id"):
        return redirect(url_for('login'))

    if request.args.get("id"):
        rowid = int(request.args.get("id"))
        crud_delete_recipe(rowid)
        return redirect(url_for('recipes'))

    abort(500)


# Shopping list
#=================================================
@app.route("/shopping_list", methods=["GET", "POST"])
def shopping_list():
    if not request.cookies.get("user_id"):
        return redirect(url_for('login'))

    uid = request.cookies.get("user_id")
    if request.method == "POST":

        item = request.form["item"]
        quan = request.form["quan"]
        crud_add_item(uid, item, quan)

    sl = crud_get_item(uid)
    return render_template("shopping_list.html", sl=sl)

# Delete item
#==================================================
@app.route("/delete_item", methods=["GET"])
def delete_item():
    if not request.cookies.get("user_id"):
        return redirect(url_for('login'))

    if request.args.get("id"):
        rowid = int(request.args.get("id"))
        crud_delete_item(rowid)
        return redirect(url_for('shopping_list'))

    abort(500)


# Meal Planner
@app.route("/meal_planner", methods=["GET", "POST"])
def meal_planner():
    if not request.cookies.get("user_id"):
        return redirect(url_for("login"))

    uid = request.cookies.get("user_id")
    if request.method == "POST":
        day = request.form["d"]
        meal_type = request.form["mt"]
        recipe = request.form["rid"]

        crud_add_meal(day, meal_type, recipe, uid)

    mp = crud_get_meal(uid)
    recipes = crud_get_recipes(uid)
    return render_template("meal_planner.html", recipes=recipes, mp=mp)
