import pytest
from sorting_algorithms.mergesort import merge_sort

def test_merge_sort_basic():
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    assert arr == [5, 6, 7, 11, 12, 13]

def test_merge_sort_empty():
    arr = []
    merge_sort(arr)
    assert arr == []

def test_merge_sort_single_element():
    arr = [42]
    merge_sort(arr)
    assert arr == [42]

def test_merge_sort_duplicates():
    arr = [3, 1, 2, 3, 1]
    merge_sort(arr)
    assert arr == [1, 1, 2, 3, 3]

def test_merge_sort_sorted_input():
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_input():
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]
