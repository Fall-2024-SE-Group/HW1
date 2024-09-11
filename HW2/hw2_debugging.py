"""
Module for merge sort and array randomization.
"""

import rand

def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        input_arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left_arr (list): The left half of the sorted array.
        right_arr (list): The right half of the sorted array.

    Returns:
        list: The merged and sorted array.
    """
    left_index, right_index = 0, 0
    merge_arr = []  # Initialize as an empty list

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Append the remaining elements from both arrays
    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


# Generate a random array using the rand module
arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)

