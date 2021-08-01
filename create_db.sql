-- Cook50 Database

CREATE TABLE recipe(
       id INT PRIMARY KEY,
       name TEXT NOT NULL,
       rating INT NOT NULL,
       difficulty TEXT NOT NULL,
       type TEXT NOT NULL,
       prep_time INT NOT NULL,
       main_ingredients TEXT NOT NULL,
       recipe_link TEXT NOT NULL
);
