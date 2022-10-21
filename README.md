# Assignment 7: Using Libraries

## Summary
In this assignment, we are learning to use Python libraries like `pandas`.
We first create a few functions to practice `numpy` data creation and file manipulation.
We are also given a file called `iris.data`, which contains data on the sepal/petal length/width of iris species, and asked to create different types of plots using `matplotlib`.

## Functions and Scripts
We create 3 functions using `numpy` standard methods:
- `get_random_matrix()` generates a random N x M matrix with values between 0 and 1 based on the dimensions we give it
- `get_file_dimensions()` reads a CSV file and returns the dimensions of the N x M matrix of data that was within
- `write_matrix_to_file()` uses `get_random_matrix()` to generate a random matrix, then saves it to a CSV file that the user names for future use

The script `plotter.py` uses `pandas` to access the `iris.data` file and easily parse through and select certain data columns for the different plots. The `matplotlib` package is used to plot figures, and we use some style commands like removing certain plot spines and generating multi-panel figures.

## Testing
We create a `run.sh` file that applies `pycodestyle` checks to all `.py` files, runs unit testing from `test_data_processor.py`, and runs functional tests from `test_plotter.sh`. The final product of this should be 3 PNG files, showing boxplots of the different iris components and color-coded scatter plots of sepal length against sepal width.
