import pytest
# TODO: add necessary import
from ml.data import apply_label

# TODO: implement the first test. Change the function name and input as needed
def test_apply_label_low_income():
    """
    Test that label 0 maps to <=50K.

    """
    # Your code here
    assert apply_label([0]) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_apply_label_high_income():
    """
    Test that label 1 maps to >50K

    """
    # Your code here
    assert apply_label([1]) == ">50K"


# TODO: implement the third test. Change the function name and input as needed
def test_apply_label_output_type():
    """
     Test that apply_label returns a string.
    
    """
    # Your code here
    assert isinstance(apply_label([1]), str)
