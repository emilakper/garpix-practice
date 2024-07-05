import unittest
import json
from app import find_minimal_identifiers, main

class TestApp(unittest.TestCase):

    def test_find_minimal_identifiers(self):
        with open("test_data.json", 'r', encoding='utf-8') as f:
            test_data = json.load(f)
        possible_results = ["name,color\r\n", "name,size\r\n"] 
        self.assertIn(find_minimal_identifiers(test_data), possible_results)

    def test_main_with_file(self):
        test_file_path = "test_data.json"
        possible_results = ["name,color\r\n", "name,size\r\n"] 
        self.assertIn(main(file_path=test_file_path), possible_results)

if __name__ == '__main__':
    unittest.main()
