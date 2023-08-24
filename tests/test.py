import sys
from src.main import File
import unittest
import os


class TestLargestValues(unittest.TestCase):
    def test_file_exists_true(self):
        file_path = File(os.path.abspath("files/tests/test_format_error.txt"))
        self.assertTrue(File.file_exists(file_path))

    def test_file_exists_false(self):
        file_path = File(os.path.abspath("files/tests/invalid_filename.txt"))
        self.assertFalse(File.file_exists(file_path))

    def test_directory_input_true(self):
        file_path = File(os.path.abspath("files/tests/"))
        self.assertTrue(File.is_directory(file_path))

    def test_directory_input_false(self):
        file_path = File(os.path.abspath("files/tests/test_format_error.txt"))
        self.assertFalse(File.is_directory(file_path))

    def test_sort_dict_values(self):
        dic = {
            "http://api.tech.com/item/121345": 9,
            "http://api.tech.com/item/122345": 350,
            "http://api.tech.com/item/123345": 25,
            "http://api.tech.com/item/124345": 231,
        }
        sorted_dic_values = File.sort_dict_values_desc(dic).values()
        self.assertGreater(list(sorted_dic_values)[0], list(sorted_dic_values)[1])

    def test_get_max_values(self):
        dic = {
            "http://api.tech.com/item/121345": 9,
            "http://api.tech.com/item/122345": 350,
            "http://api.tech.com/item/123345": 25,
            "http://api.tech.com/item/124345": 231,
        }
        max_values = 2
        self.assertEqual(len(File.get_max_values(dic, max_values)), max_values)

    def test_continue_file_iteration_1(self):
        file_path = File(os.path.abspath("files/tests/test_float.txt"))
        self.assertEqual(len(File.file_iterator(file_path)), 3)

    def test_continue_file_iteration_2(self):
        file_path = File(os.path.abspath("files/tests/test_format_error.txt"))
        self.assertEqual(len(File.file_iterator(file_path)), 2)

    def test_continue_file_iteration_3(self):
        file_path = File(os.path.abspath("files/tests/test_invalid_order.txt"))
        self.assertEqual(len(File.file_iterator(file_path)), 0)


if __name__ == "__main__":
    sys.path.append(sys.path[0] + "/..")
    unittest.main()