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

def save_and_close_db():
	connection.commit()
	connection.close()

def main():
	generate_database()
	save_and_close_db()

if __name__ == '__main__':
	main()