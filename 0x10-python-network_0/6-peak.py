#!/usr/bin/python3
""" Finds the peak in a list """
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    list_of_integers (list): The list of unsorted integers.

    Returns:
    int: A peak element from the list.

    Complexity:
    O(log(n))
    """

    def binary_search_peak(arr, left, right):
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            return binary_search_peak(arr, mid + 1, right)
        else:
            return binary_search_peak(arr, left, mid)

    if not list_of_integers:
        return None

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
