import sqlite3

connection = sqlite3.connect("store_operations.db")
cursor = connection.cursor()

def create_table_customers():
	query = "CREATE TABLE IF NOT EXISTS customer_info (shopper_id INTEGER PRIMARY KEY, customer_name TEXT, email TEXT)"
	cursor.execute(query) 

def display_customer_table():
	query = "SELECT * FROM customer_info"
	table = cursor.execute(query)
	for row in table:
		print("[" + str(row[0]) + "]" + "[" + " -- [" + row[1] + "]" + " -- [" + str(row[2]) + "]")

def insert_customer_details(value1, value2):
	query = "INSERT INTO customer_info (customer_name, email) VALUES (?, ?)"
	cursor.execute(query, (value1, value2))

def update_customer_name(customer_name, customer_id):
	query = "UPDATE customer_info SET customer_name = ? WHERE shopper_id = ?"
	cursor.execute(query, (customer_name, customer_id))

def update_customer_email(customer_email, customer_id):
	query = "UPDATE customer_info SET email = ? WHERE shopper_id = ?"
	cursor.execute(query, (customer_email, customer_id))

def create_table_catalogue():
	query = "CREATE TABLE IF NOT EXISTS catalogue_info (item_id INTEGER PRIMARY KEY, item_name TEXT, brand TEXT)"
	cursor.execute(query)

def create_table_purchases():
	query = "CREATE TABLE IF NOT EXISTS purchases_info (purchases_id INTEGER PRIMARY KEY, date_time DATETIME, FOREIGN KEY (item_id) REFERENCES create_table_catalogue(item_id)"
	cursor.execute(query)

def save_and_close_db():
	connection.commit()
	connection.close()

def main():
	create_table_customers()
	display_customer_table()
	# name = input("What is your name?\n")
	# email = input("What is your email?\n")
	# insert_customer_details(name, email)

	shopper_id = input("Which id do you want to change?\n")
	# new_name = input("What is the new name you want to enter?\n")
	# update_customer_name(new_name, int(shoppers_id))
	new_email = input("What is the new email of this person?\n")
	update_customer_email(new_email, int(shopper_id))

	save_and_close_db()

# create_table_catalogue()
# create_table_purchases()


if __name__ == '__main__':
	main()