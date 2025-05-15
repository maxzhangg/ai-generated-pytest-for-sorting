import pytest
from sorting_algorithms.quicksort import quick_sort

def test_quick_sort_normal():
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 5, 7, 8, 9, 10]

def test_quick_sort_empty():
    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == []

def test_quick_sort_single_element():
    arr = [42]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [42]

def test_quick_sort_duplicates():
    arr = [3, 1, 2, 3, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 3, 3]

def test_quick_sort_sorted_input():
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_input():
    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]
