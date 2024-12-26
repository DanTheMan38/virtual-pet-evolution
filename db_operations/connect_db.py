import mysql.connector
from db_operations.logger import log_info, log_error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Daniel",  # Use the password you set
            database="virtual_pet_db"
        )
        if connection.is_connected():
            log_info("Connected to the database successfully.")
            print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        log_error(f"Error connecting to the database: {err}")
        print(f"Error: {err}")
        return None