import mysql.connector
from datetime import datetime
from db_operations.connect_db import connect_to_db
from db_operations.logger import logger

def update_last_interaction(pet_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Define the new last interaction time
        new_time = datetime.now()

        # Update query
        query = "UPDATE pets SET last_interaction = %s WHERE id = %s"
        values = (new_time, pet_id)

        # Execute and commit the update
        cursor.execute(query, values)
        connection.commit()

        logger.info(f"Pet ID {pet_id} last_interaction updated to {new_time}")
        print(f"Pet ID {pet_id} last_interaction updated to {new_time}")
    except mysql.connector.Error as err:
        logger.error(f"Error updating last_interaction for Pet ID {pet_id}: {err}")
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Replace '1' with the pet ID you want to update
if __name__ == "__main__":
    update_last_interaction(1)