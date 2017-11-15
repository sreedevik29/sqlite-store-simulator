import sqlite3

connection = sqlite3.connect("store_operations.db")
cursor = connection.cursor()

def create_customer_table():
	query = "CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
	cursor.execute(query) 

def create_catalogue_table():
	query = "CREATE TABLE IF NOT EXISTS catalogue (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price INTEGER, available BOOLEAN DEFAULT 1)"
	cursor.execute(query)

def create_purchase_table():
	query = """ CREATE TABLE IF NOT EXISTS purchase(
				id INTEGER PRIMARY KEY, 
				date_time DATETIME, 
				shopper_id INTEGER, 
				item_id INTEGER, 
				price INTEGER,
				FOREIGN KEY (item_id) REFERENCES catalogue(id),
				FOREIGN KEY (price) REFERENCES catalogue(price),
				FOREIGN KEY (shopper_id) REFERENCES customer(id))"""
	cursor.execute(query)

def generate_database():
	create_customer_table()
	create_catalogue_table()
	create_purchase_table()

def prompt_user_input():
	user_info = {"name": "", "email": ""}
	user_info["name"] = input("What is your name?\n")
	user_info["email"] = input("What is your email?\n")
	return user_info

def create_new_user(user_info):
	name = user_info["name"]
	email = user_info["email"]
	query = "INSERT INTO customer (name, email) VALUES (?, ?)"
	cursor.execute(query, (name, email))

def register_user():
	user_info = prompt_user_input()
	create_new_user(user_info)

def prompt_item_input():
	item_info = {"name": "jeans", "category": "clothing", "price": ""}
	item_info["name"] = input("What is the name of the item?\n")
	item_info["category"] = input("Which category is the item from?\n")
	item_info["price"] = int(input("What is price of that item?\n"))
	return item_info

def add_new_items(item_info):
	name = item_info["name"]
	category = item_info["category"]
	price = item_info["price"]
	query = "INSERT INTO catalogue (name, category, price) VALUES (?, ?, ?)"
	cursor.execute(query, (name, category, price))

def new_inventory():
	item_info = prompt_item_input()
	add_new_items(item_info)

def save_and_close_db():
	connection.commit()
	connection.close()

def main():
	generate_database()
	register_user()
	new_inventory()
	save_and_close_db()

if __name__ == '__main__':
	main()