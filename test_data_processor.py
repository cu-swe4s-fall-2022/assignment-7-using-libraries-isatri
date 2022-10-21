"""This tests the functions in data_processor using positive, negative,
and assertion raise tests.

"""
import sys
import os
import unittest
import numpy as np
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(src_path)
import data_processor as dp  # nopep8


class TestDataProcessor(unittest.TestCase):

    def test_get_random_matrix(self):
        r_mat = dp.get_random_matrix(self.N, self.M)

        self.assertTrue(r_mat.shape == (self.N, self.M))
        self.assertTrue(np.all((r_mat > 0) & (r_mat <= 1)))
        self.assertFalse(np.any((r_mat < 0) & (r_mat >= 1)))
        self.assertRaises(ValueError, dp.get_random_matrix, 0, self.M)
        self.assertRaises(ValueError, dp.get_random_matrix, -20, self.M)
        self.assertRaises(TypeError, dp.get_random_matrix, 'a', self.M)

    def test_get_file_dimensions(self):
        self.assertEqual(dp.get_file_dimensions(self.file_name),
                         (self.N, self.M))
        self.assertNotEqual(dp.get_file_dimensions(self.file_name),
                            (0, self.N))
        self.assertRaises(TypeError, dp.get_file_dimensions, 0)
        self.assertRaises(TypeError, dp.get_file_dimensions, 1.0)
        self.assertRaises(FileNotFoundError, dp.get_file_dimensions, 'bla.csv')

    def test_write_matrix_to_file(self):
        recovered_matrix = np.genfromtxt(self.file_name, delimiter=',')

        self.assertTrue(recovered_matrix.shape == (self.N, self.M))
        self.assertFalse(recovered_matrix.shape != (self.N, self.M))
        self.assertRaises(TypeError, dp.write_matrix_to_file,
                          self.N, self.M, 0.0)
        self.assertRaises(TypeError, dp.write_matrix_to_file,
                          self.N, self.M, 5)
        self.assertRaises(TypeError, dp.write_matrix_to_file,
                          self.N, 'a', self.file_name)
        self.assertRaises(ValueError, dp.write_matrix_to_file,
                          0, self.M, self.file_name)

    def setUp(self):
        self.N = int(np.random.randint(2, 10, 1))
        self.M = int(np.random.randint(2, 10, 1))

        self.file_name = 'temp_mat.csv'
        dp.write_matrix_to_file(self.N, self.M, self.file_name)

    def tearDown(self):
        self.N = 0
        self.M = 0
        os.remove(self.file_name)


if __name__ == "__main__":
    unittest.main()
