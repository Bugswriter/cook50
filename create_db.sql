-- Cook50 Database

-- USER TABLE
CREATE TABLE user(
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    join_date TEXT NOT NULL,
    password TEXT NOT NULL
);

-- RECIPE TABLE
CREATE TABLE recipe(
    name TEXT NOT NULL,
    rating INT NOT NULL,
    difficulty TEXT NOT NULL,
    type TEXT NOT NULL,
    prep_time INT NOT NULL,
    main_ingredients TEXT NOT NULL,
    recipe_link TEXT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(rowid)
);

-- SHOPPING LIST TABLE
CREATE TABLE shopping_list(
    item TEXT NOT NULL,
    quantity INT,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(rowid)
);
