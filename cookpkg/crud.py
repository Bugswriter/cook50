#=================
# CRUD Functions #
#=================
import sqlite3

DB_NAME="site.db"

# CRUD function for adding new user
#==================================================
def register_user(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    values = "('{}','{}', date(), '{}')".format(data['u'], data['e'], data['p'])
    sql = "INSERT INTO user VALUES {}".format(values)
    try:
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])

    conn.close()

# CRUD function for checking login credentials
#==================================================
def check_login_cred(u, p):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    sql = "SELECT rowid, * FROM user WHERE username='{}' AND password='{}' LIMIT 1".format(u, p)
    out = c.execute(sql)
    return out.fetchone()


# CRUD funciton for adding new recipe
#==================================================
def crud_add_recipe(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    values = "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(data['n'], data['r'], data['d'], data['rt'], data['pt'], data['mi'], data['rl'], data['ui'])
    sql = "INSERT INTO recipe VALUES {}".format(values)
    try:
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: " , e.args[0])

    conn.close()

# CRUD function for getting recipes
#==================================================
def crud_get_recipes(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    data = []
    sql = "SELECT rowid, * FROM recipe WHERE user_id='{}'".format(uid)
    for row in c.execute(sql):
        data.append(list(row))

    conn.close()
    return data


# CRUD function for deleting recipe
#==================================================
def crud_delete_recipe(rowid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        sql = "DELETE FROM recipe WHERE rowid={}".format(rowid)
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])

    conn.close()


# CRUD Add Item
#=================================================
def crud_add_item(uid, item, quan):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        values = "('{}','{}', '{}')".format(item, quan, uid)
        sql = "INSERT INTO shopping_list VALUES {}".format(values)
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])

    conn.close()


# CRUD Get Item
#=================================================
def crud_get_item(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    sql = "SELECT rowid, * FROM shopping_list WHERE user_id={}".format(uid)
    data = []
    for row in c.execute(sql):
        data.append(list(row))

    conn.close()
    return data


# CRUD function for deleting item
#==================================================
def crud_delete_item(rowid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        sql = "DELETE FROM shopping_list WHERE rowid={}".format(rowid)
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])

    conn.close()


# CRUD function for adding meal
#===================================================
def crud_add_meal(d, mt, rid, uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        cond = "WHERE day='{}' AND meal_type='{}' AND user_id={}".format(d, mt, uid)
        query = "SELECT rowid, * FROM meal_planner {}".format(cond)
        out = c.execute(query)
        if out.fetchone():
            sql = "UPDATE meal_planner SET recipe_id={} {}".format(rid, cond)
        else:
            values = "('{}','{}', '{}', '{}')".format(d, mt, rid, uid)
            sql = "INSERT INTO meal_planner VALUES {}".format(values)
            
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])

    conn.close()    


# CRUD function for getting meal
#===================================================    
def crud_get_meal(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        sql = "SELECT rowid, * FROM meal_planner WHERE user_id={}".format(uid)
        data = []
        for row in c.execute(sql):
            data.append(list(row))

    except sqlite3.Error as e:
        print("An error occured: ", e.args[0])
        
    return data
