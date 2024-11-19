import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Daniel",  # Use the password you set
            database="virtual_pet_db"
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None