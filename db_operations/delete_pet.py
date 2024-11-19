import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_operations.connect_db import connect_to_db
import mysql.connector

def delete_pet(pet_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "DELETE FROM pets WHERE id = %s"
        cursor.execute(query, (pet_id,))
        connection.commit()
        print(f"Pet ID {pet_id} deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Replace '1' with the ID of the pet you want to delete
delete_pet(1)