 
import pytest
from sorting_algorithms.selectionsort import selection_sort

def test_selection_sort_basic():
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr, len(arr))
    assert arr == [11, 12, 22, 25, 64]

def test_selection_sort_empty():
    arr = []
    selection_sort(arr, len(arr))
    assert arr == []

def test_selection_sort_single():
    arr = [42]
    selection_sort(arr, len(arr))
    assert arr == [42]

def test_selection_sort_duplicates():
    arr = [5, 3, 5, 3, 2]
    selection_sort(arr, len(arr))
    assert arr == sorted(arr)

def test_selection_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    selection_sort(arr, len(arr))
    assert arr == [1, 2, 3, 4, 5]

def test_selection_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    selection_sort(arr, len(arr))
    assert arr == [1, 2, 3, 4, 5]
