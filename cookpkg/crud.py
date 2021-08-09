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
def crud_get_recipes(uid, offset):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    data = []
    sql = "SELECT rowid, * FROM recipe WHERE user_id='{}' LIMIT 10 OFFSET {}".format(uid, offset)
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
