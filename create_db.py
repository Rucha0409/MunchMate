import sqlite3
conn = sqlite3.connect('munchmate.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Recipes")
c.execute('''CREATE TABLE Recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    prep_time TEXT,
    ingredients TEXT,
    recipe TEXT,
    image TEXT
)''')
recipes = [
 ("Aloo Paratha","Breakfast / Lunch","25 min","Wheat flour, boiled potatoes, chili, coriander, salt, oil/ghee","Mash potatoes with spices → stuff into dough → roll → cook on tawa with ghee till golden.","aloo_paratha.jpg"),
 ("Poha","Breakfast / Snack","15 min","Poha, onion, green chili, curry leaves, mustard seeds, turmeric, lemon juice, peanuts","Rinse poha → sauté mustard, curry leaves, onion, peanuts → add turmeric + poha + salt → cook 2–3 min → add lemon.","poha.jpg"),
 ("No-Bake Chocolate Biscuit Cake","Dessert","15 min","Marie biscuits, cocoa, sugar, butter, milk","Crush biscuits → mix with cocoa & milk → set in tin → refrigerate 2 hrs.","chocolate_biscuit_cake.jpg"),
 ("Dal Tadka","Lunch / Dinner","30 min","Toor dal, onion, tomato, garlic, ghee, cumin, chili, turmeric","Cook dal → temper with ghee, cumin, garlic & chili → pour over dal.","dal_tadka.jpg"),
 ("Grilled Veg Sandwich","Breakfast / Snack","10 min","Bread, butter, cucumber, tomato, cheese, green chutney","Spread chutney & butter → layer veggies & cheese → grill till crispy.","grilled_veg_sandwich.jpg"),
 ("Fried Rice","Lunch / Dinner","20 min","Cooked rice, soy sauce, onion, capsicum, carrot, salt, pepper","Stir-fry veggies → add rice + soy sauce → toss on high flame.","fried_rice.jpg"),
 ("Rava Kesari","Indian Sweet / Dessert","15 min","Rava, sugar, ghee, water, saffron, cashews","Roast rava in ghee → add hot water + sugar → stir till thick → garnish.","rava_kesari.jpg"),
 ("Besan Chilla","Breakfast / Snack","15 min","Besan, onion, chili, coriander, water, salt","Mix batter → pour on tawa → cook both sides till golden.","besan_chilla.jpg"),
 ("Creamy White Sauce Pasta","Lunch / Dinner","20 min","Pasta, butter, flour, milk, cheese, pepper, herbs","Boil pasta → make sauce (butter + flour + milk) → mix with pasta & cheese.","white_sauce_pasta.jpg"),
 ("Mango Lassi","Drink / Dessert","5 min","Curd, mango pulp, sugar, cardamom","Blend all till smooth → chill & serve.","mango_lassi.jpg")
]
c.executemany("INSERT INTO Recipes (name, type, prep_time, ingredients, recipe, image) VALUES (?,?,?,?,?,?)", recipes)
conn.commit()
conn.close()
print('munchmate.db created with 10 recipes')