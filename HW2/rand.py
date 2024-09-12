"""
This module provides a function to fill an array with random integers
between 1 and 20.
"""
import random

def random_array(arr):
    """
    Fills the array with random integers between 1 and 20.
    
    Args:
        arr (list): The array to be filled with random numbers.

    Returns:
        list: The array filled with random integers.
    """
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
