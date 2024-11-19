import mysql.connector
from datetime import datetime

try:
    # Establish connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Daniel",  # Use your updated root password
        database="virtual_pet_db"
    )
    cursor = connection.cursor()

    # Define the pet ID and new last interaction time
    pet_id = 1  # Change this ID to update a specific pet
    new_time = datetime.now()

    # Update query
    query = "UPDATE pets SET last_interaction = %s WHERE id = %s"
    values = (new_time, pet_id)

    # Execute and commit the update
    cursor.execute(query, values)
    connection.commit()
    print(f"Pet ID {pet_id} last_interaction updated to {new_time}")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()