"""
Module for merge sort and array randomization.
"""

import rand

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left_arr (list): The left half of the sorted array.
        right_arr (list): The right half of the sorted array.

    Returns:
        list: The merged and sorted array.
    """
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged.append(left_arr[left_index])
            left_index += 1
        else:
            merged.append(right_arr[right_index])
            right_index += 1

    # Append the remaining elements from both arrays
    merged.extend(left_arr[left_index:])
    merged.extend(right_arr[right_index:])

    return merged


def main():
    """
    Generates a random array, sorts it, and outputs the sorted array.
    """
    rand_arr = rand.random_array([None] * 20)
    sorted_arr = merge_sort(rand_arr)

    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
