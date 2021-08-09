from cookpkg import app
from cookpkg.crud import *
from flask import request, render_template, redirect, url_for, flash, make_response

#==================
# Route Functions #
#==================

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
    offset = 0
    if request.args.get('page'):
        page = int(request.args.get('page'))
        offset = 10 * (page - 1)

    data = crud_get_recipes(uid, offset)
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

    if request.method == "POST":
        crud_add_item(request.cookies.get("user_id"), request.form["item"])

    # one comment
    sl = []
    return render_template("shopping_list.html", shopping_list=sl)
