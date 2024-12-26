import unittest
from db_operations.delete_pet import delete_pet
from db_operations.connect_db import connect_to_db

class TestDeletePet(unittest.TestCase):
    def setUp(self):
        # Prepare a test database entry
        self.connection = connect_to_db()
        self.cursor = self.connection.cursor()
        self.test_pet = {"id": 999, "name": "TestPet", "type": "TestType", "age": 1, "evolution_stage": 1}
        self.cursor.execute(
            "INSERT INTO pets (id, name, type, age, evolution_stage) VALUES (%s, %s, %s, %s, %s)",
            (self.test_pet["id"], self.test_pet["name"], self.test_pet["type"], self.test_pet["age"], self.test_pet["evolution_stage"]),
        )
        self.connection.commit()

    def test_delete_existing_pet(self):
        # Test the deletion of the test pet
        delete_pet(self.test_pet["id"])
        self.cursor.execute("SELECT * FROM pets WHERE id = %s", (self.test_pet["id"],))
        result = self.cursor.fetchone()
        self.assertIsNone(result, "Pet was not deleted successfully.")

    def tearDown(self):
        # Clean up the database
        self.cursor.execute("DELETE FROM pets WHERE id = %s", (self.test_pet["id"],))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    unittest.main()