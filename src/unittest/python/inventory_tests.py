import unittest
from validator import validate_temperature

class TestInventory(unittest.TestCase):
    def test_range_temperature(self):
        # Probamos que 4 sea válido (True) y 0 sea inválido (False)
        self.assertTrue(validate_temperature(4))
        self.assertFalse(validate_temperature(0))
        self.assertTrue(validate_temperature(2))
        self.assertTrue(validate_temperature(8))

if __name__ == '__main__':
    unittest.main()