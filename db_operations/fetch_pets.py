import sys
import os
import logging
import mysql.connector

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_operations.connect_db import connect_to_db
from db_operations.logger import logger

def fetch_pets():
    pets = []  # Initialize an empty list to ensure a consistent return type
    try:
        # Connect to the database
        connection = connect_to_db()
        cursor = connection.cursor()

        # Fetch all pets from the database
        cursor.execute("SELECT * FROM pets")
        pets = cursor.fetchall()

        # Log the fetched pets
        if pets:
            logger.info(f"Fetched pets: {pets}")
        else:
            logger.info("No pets found in the database.")

    except mysql.connector.Error as err:
        logger.error(f"Error fetching pets: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return pets  # Ensure the function always returns a list

# Run the function
if __name__ == "__main__":
    fetched_pets = fetch_pets()
    for pet in fetched_pets:
        print(pet)