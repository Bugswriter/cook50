-- Cook50 Database

CREATE TABLE recipe(
    name TEXT NOT NULL,
    rating INT NOT NULL,
    difficulty TEXT NOT NULL,
    type TEXT NOT NULL,
    prep_time INT NOT NULL,
    main_ingredients TEXT NOT NULL,
    recipe_link TEXT NOT NULL
);
