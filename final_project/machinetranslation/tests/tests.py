import unittest
from translator import french_to_english, english_to_french

class TestMachineTranslation(unittest.TestCase):

    def test_fr_en_null(self):
        self.assertNotEqual(french_to_english("not null"),None,"null input")

    def test_fr_en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_en_fr_null(self):
        self.assertNotEqual(english_to_french("not null"),None,"null input")

    def test_en_fr(self):
        self.assertEqual(french_to_english('Hello'), 'Bonjour')

if __name__ == "__main__":
    unittest.main()