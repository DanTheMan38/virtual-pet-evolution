import sys
import os
import logging
import mysql.connector

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_operations.connect_db import connect_to_db
from db_operations.logger import logger

def get_pets_by_criteria(pet_type=None, evolution_stage=None):
    try:
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)

        # Base query
        query = "SELECT * FROM pets WHERE 1=1"
        params = []

        # Add conditions based on provided criteria
        if pet_type:
            query += " AND type = %s"
            params.append(pet_type)
        if evolution_stage:
            query += " AND evolution_stage = %s"
            params.append(evolution_stage)

        cursor.execute(query, params)
        results = cursor.fetchall()

        if results:
            logger.info(f"Pets matching criteria: {results}")
            print("Pets matching criteria:")
            for pet in results:
                print(f"ID: {pet['id']}, Name: {pet['name']}, Type: {pet['type']}, Age: {pet['age']}, Evolution Stage: {pet['evolution_stage']}, Last Interaction: {pet['last_interaction']}")
        else:
            logger.info("No pets matching the criteria were found.")
            print("No pets matching the criteria were found.")

    except mysql.connector.Error as err:
        logger.error(f"Error filtering pets: {err}")
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
# Replace the values below with the criteria you want to use for filtering
if __name__ == "__main__":
    get_pets_by_criteria(pet_type="Fire", evolution_stage=1)