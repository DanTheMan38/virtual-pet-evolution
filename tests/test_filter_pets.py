import unittest
from db_operations.filter_pets import filter_pets

class TestFilterPets(unittest.TestCase):
    def test_filter_pets(self):
        # Test filtering with specific criteria
        pets = filter_pets(pet_type="Electric", evolution_stage=2)
        self.assertIsInstance(pets, list, "Filtered pets should be a list.")
        self.assertGreater(len(pets), 0, "Filtered pets list should not be empty.")
        for pet in pets:
            self.assertEqual(pet["type"], "Electric")
            self.assertEqual(pet["evolution_stage"], 2)

    def test_no_matching_pets(self):
        # Test when no pets match the criteria
        pets = filter_pets(pet_type="NonexistentType", evolution_stage=999)
        self.assertIsInstance(pets, list, "Filtered pets should be a list.")
        self.assertEqual(len(pets), 0, "Filtered pets list should be empty for nonexistent criteria.")

if __name__ == "__main__":
    unittest.main()