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

def select_item_ID():
	item_id = input("What is the ID# of the item?\n")
	return item_id

def update_item_availability(item_id):
	query = "UPDATE catalogue SET available = 0 WHERE id = ?"
	cursor.execute(query, (item_id))

def new_availability_status():
	item_id = select_item_ID()
	update_item_availability(item_id)

def select_user_ID():
	user_id = input("What is the ID of the customer you want to select?\n")
	return user_id

def prompt_new_customer_name():
	user_name = input("What is the new name of this customer?\n")
	return user_name

def new_customer_name(user_name, user_id):
	query = "UPDATE customer SET name = ? WHERE id = ?"
	cursor.execute(query, (user_name, user_id))

def update_customer_name():
	user_id = select_user_ID()
	user_name = prompt_new_customer_name()
	new_customer_name(user_name, user_id)

def prompt_new_customer_email():
	user_email = input("What is the new email of this customer?\n")
	return user_email

def new_customer_email(user_email, user_id):
	query = "UPDATE customer SET email = ? WHERE id = ?"
	cursor.execute(query, (user_email, user_id))

def update_customer_email():
	user_id = select_user_ID()
	user_email = prompt_new_customer_email()
	new_customer_email(user_email, user_id)

def save_and_close_db():
	connection.commit()
	connection.close()

def main():
	generate_database()

	active = True

	while active:
		user_input = input("Select option: [ 1 - Register user, 2 - Add new inventory item, 3 - Update availability status of item, 4 - Update customer name, 5 - Update customer email, 6 - EXIT ]\n")
		if user_input == "1":
			register_user()
		elif user_input == "2":
			new_inventory()
		elif user_input == "3":
			new_availability_status()
		elif user_input == "4":
			update_customer_name()
		elif user_input == "5":
			update_customer_email()
		else:
			active = False
	
	save_and_close_db()

if __name__ == '__main__':
	main()