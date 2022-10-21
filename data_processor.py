#!/usr/bin/python -tt
"""Functions for processing data in Assignment 7

    * get_random_matrix - returns an NxM Numpy matrix of random (0,1] values
	* get_file_dimensions - returns the dimensions of data from a read CSV file
	* write_matrix_to_file - generates random NxM matrix and saves to CSV file

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
	# Catch inappropriate data types/values
	if type(num_rows) != int or type(num_columns) != int:
		raise TypeError('Matrix dimensions must be integers.')
	elif num_rows <= 0 or num_columns <= 0:
		raise ValueError('Matrix dimensions must be > 0.')

	return np.random.rand(num_rows, num_columns)


def get_file_dimensions(file_name):
	"""Takes the name of a CSV file, reads it, and returns the dimensions of
	the tabulated data within.

    Parameters
    ----------
    file_name : str
		The name of the file to read data from

    Returns
    -------
    file.shape : tuple of int
        The dimensions of the tabular data in the CSV file

    """
	if type(file_name) != str:  # Catch inappropriate input types
		raise TypeError('File name must be a string of characters.')

	file = np.genfromtxt(file_name, delimiter=',')
	return file.shape


def write_matrix_to_file(num_rows, num_columns, file_name):
	"""Creates an NxM Numpy matrix of random (0,1] values and saves it to a
	CSV file with a user inputted name.

    Parameters
    ----------
    num_rows : int
        Number of rows for the generated random matrix
    num_columns : int
        Number of colums for the generated random matrix
    file_name : str
		The name of the CSV file to save

    Returns
    -------

    """
	if type(file_name) != str:  # Catch inappropriate input types
		raise TypeError('File name must be a string of characters.')

	random_matrix = get_random_matrix(num_rows, num_columns)
	np.savetxt(file_name, random_matrix, delimiter=",")
