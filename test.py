"""
This is a testing file to test the plotting functions found in main.py. All of
the tests are conducted using the test_data.csv file, which is a test file that
contains fake data purely for the sake of testing the correctness of each
plotting function. The data is constructed in a way that one can predict how
the plot should look like, provided they know what data each function plots on
each axis.
"""
from age import plot_age
from alcohol import plot_alcohol
from caffeine import plot_caffeine
from exercise import plot_exercise
from smoking import plot_smoking

import pandas as pd


TEST_DATA_FILE_NAME = "test_data.csv"


def test_with_this_data(data: pd.DataFrame,
                        age: bool = False,
                        alcohol: bool = False,
                        caffeine: bool = False,
                        exercise: bool = False,
                        smoking: bool = False) -> None:
    """
    Accepts a pandas data frame and creates plots using the data. Used for
    manual testing purposes, meaning there is no hard "tests." This function
    simply produces the chosen plots, while their accuracy or "correctness" is
    left to the user's discretion.
    Also accepts bool values for age, alcohol, caffeine, exercise, and smoking.
    A True value will plot the respective data while False (default value) will
    not produce any plots for that data.
    """
    if age:
        plot_age(data)
    if alcohol:
        plot_alcohol(data)
    if caffeine:
        plot_caffeine(data)
    if exercise:
        plot_exercise(data)
    if smoking:
        plot_smoking(data)


def main():
    print("RUNNING TESTS")
    data = pd.read_csv(TEST_DATA_FILE_NAME)
    data = pd.get_dummies(data)
    test_with_this_data(
        data,
        True,  # age
        True,  # alcohol
        True,  # caffeine
        True,  # exercise
        True   # smoking
    )


if __name__ == "__main__":
    main()
