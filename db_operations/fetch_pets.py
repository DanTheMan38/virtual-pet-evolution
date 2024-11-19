import mysql.connector

def fetch_pets():
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Daniel',  # Replace with your actual root password
            database='virtual_pet_db'
        )

        # Create a cursor to execute queries
        cursor = connection.cursor()

        # Fetch all pets from the database
        cursor.execute("SELECT * FROM pets")
        pets = cursor.fetchall()

        # Print the fetched pets
        for pet in pets:
            print(pet)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the function
if __name__ == "__main__":
    fetch_pets()