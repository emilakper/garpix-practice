import unittest
import os
from django.test import TestCase
import app
from core.utils import load_data_from_json, get_attribute_frequency


class AppTestCase(TestCase):

    def test_find_minimal_identifiers(self):
        """Тест функции поиска минимального набора идентификаторов."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(test_dir, 'test_data.json')
        with open(file_path, 'r', encoding='utf-8'):
            test_data = load_data_from_json(file_path)

        possible_results = ["name,color", "name,size"]
        self.assertIn(app.find_minimal_identifiers(test_data), possible_results)

    def test_main_with_file(self):
        """Тест функции main с указанием пути к файлу."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        test_file_path = os.path.join(test_dir, 'test_data.json')

        possible_results = ["name,color", "name,size"]
        self.assertIn(app.main(file_path=test_file_path), possible_results)

    def test_load_data_from_json(self):
        """Тест функции load_data_from_json."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(test_dir, 'test_data.json')

        data = load_data_from_json(file_path)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)

        with self.assertRaises(ValueError):
            load_data_from_json("non_existent_file.json")

    def test_get_attribute_frequency(self):
        """Тест функции get_attribute_frequency."""
        test_data = [
            {"a": 1, "b": 2, "c": "hello"},
            {"a": 2, "b": 2, "c": "world"},
            {"a": 1, "b": 3, "c": "hello"}
        ]
        expected_result = [('a', {1, 2}), ('b', {2, 3}), ('c', {'hello', 'world'})]
        result = get_attribute_frequency(test_data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
