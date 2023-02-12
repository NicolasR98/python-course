import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'hello'
        expected = 'Hello'
        result = cap.cap_text(text)
        self.assertEqual(result, expected)
    
    def test_multiple_words(self):
        text = 'hello world'
        expected = 'Hello World'
        result = cap.cap_text(text)
        self.assertEqual(result, expected)
        
if __name__ == '__main__':
    # When running the script, run this code block
    unittest.main()