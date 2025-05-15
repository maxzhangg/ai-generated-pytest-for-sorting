# tests/test_insertion_sort.py

import pytest
from sorting_algorithms.insertionsort import insertion_sort

def test_insertion_sort():
    # Test a normal array
    arr = [12, 11, 13, 5, 6, 7]
    insertion_sort(arr, len(arr))
    assert arr == [5, 6, 7, 11, 12, 13]

    # Test an empty array
    arr = []
    insertion_sort(arr, len(arr))
    assert arr == []

    # Test a single-element array
    arr = [1]
    insertion_sort(arr, len(arr))
    assert arr == [1]

    # Test an array with duplicate elements
    arr = [5, 1, 5, 3, 5, 3]
    insertion_sort(arr, len(arr))
    assert arr == [1, 3, 3, 5, 5, 5]

    # Test an already sorted array
    arr = [1, 2, 3, 4, 5]
    insertion_sort(arr, len(arr))
    assert arr == [1, 2, 3, 4, 5]

    # Test a descending array
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertion_sort(arr, len(arr))
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
