#=================
# CRUD Functions #
#=================
import sqlite3

DB_NAME="site.db"
# CRUD funciton for adding new recipe
#==================================================
def crud_add_recipe(data):
    conn = sqlite3.connect(DB_NAME)
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
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    data = []
    for row in c.execute("SELECT rowid, * FROM recipe LIMIT 10 OFFSET {}".format(offset)):
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

