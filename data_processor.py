"""Functions for processing data in Assignment 7

    * get_random_matrix - returns an NxM Numpy matrix of random (0,1] values

"""
import numpy as np


def get_random_matrix(num_rows, num_columns):
    """Returns an NxM Numpy matrix of random (0,1] values.

    Parameters
    ----------
    num_rows : int
        Number of rows for the generated random matrix
    num_columns : int
        Number of colums for the generated random matrix

    Returns
    -------
    matrix : numpy array
        An NxM random matrix with values between (0,1]

    """
	# Catch inappropriate input types and values
	if type(num_rows) != int or type(num_columns) != int:
		raise TypeError('Matrix rows and columns must be integers.')
	elif num_rows <= 0 or num_columns <= 0:
		raise ValueError('Matrix rows and columns must be > 0.')

	return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name):
	return (0,0)


def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
