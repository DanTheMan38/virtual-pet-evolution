import sys
import os
import logging
import mysql.connector

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_operations.connect_db import connect_to_db
from db_operations.logger import logger

def update_evolution_stage(pet_id, new_stage):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "UPDATE pets SET evolution_stage = %s WHERE id = %s"
        cursor.execute(query, (new_stage, pet_id))
        connection.commit()

        logger.info(f"Pet ID {pet_id} evolution stage updated to {new_stage}.")
        print(f"Pet ID {pet_id} evolution stage updated to {new_stage}.")
    except mysql.connector.Error as err:
        logger.error(f"Error updating evolution stage for Pet ID {pet_id}: {err}")
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Replace '1' with the pet ID and '2' with the new evolution stage
if __name__ == "__main__":
    update_evolution_stage(1, 2)