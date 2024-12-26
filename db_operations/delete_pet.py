import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_operations.connect_db import connect_to_db
from db_operations.logger import logger
import mysql.connector

def delete_pet(pet_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "DELETE FROM pets WHERE id = %s"
        cursor.execute(query, (pet_id,))
        connection.commit()
        logger.info(f"Pet ID {pet_id} deleted successfully.")
    except mysql.connector.Error as err:
        logger.error(f"Error deleting pet ID {pet_id}: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Replace '1' with the ID of the pet you want to delete
delete_pet(1)