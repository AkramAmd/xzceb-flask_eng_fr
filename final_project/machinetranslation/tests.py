import unittest
from translator import french_to_english, english_to_french

class TestFrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertIsNone(french_to_english(None),"text is empty")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
class TestEnglish_to_french(unittest.TestCase):
    def test2(self):
        self.assertIsNone(english_to_french(None),"text is empty")
        self.assertEqual(french_to_english('Hello'), 'Bonjour')