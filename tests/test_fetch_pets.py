import unittest
from db_operations.fetch_pets import fetch_pets

class TestFetchPets(unittest.TestCase):
    def test_fetch_pets(self):
        pets = fetch_pets()
        self.assertIsInstance(pets, list, "Fetched pets should be a list.")
        for pet in pets:
            self.assertIsInstance(pet, tuple, "Each pet should be a tuple.")
            self.assertGreaterEqual(len(pet), 5, "Each pet tuple should have at least 5 elements.")

if __name__ == "__main__":
    unittest.main()