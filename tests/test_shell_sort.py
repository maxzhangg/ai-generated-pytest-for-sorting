 
import pytest
from sorting_algorithms.shellsort import shell_sort

def test_shell_sort_basic():
    arr = [64, 34, 25, 12, 22, 11, 90]
    inc = [5, 3, 1]
    shell_sort(arr, len(arr), inc, len(inc))
    assert arr == sorted(arr)

def test_shell_sort_empty():
    arr = []
    shell_sort(arr, len(arr), [1], 1)
    assert arr == []

def test_shell_sort_single():
    arr = [42]
    shell_sort(arr, len(arr), [1], 1)
    assert arr == [42]

def test_shell_sort_duplicates():
    arr = [5, 3, 5, 3, 2]
    shell_sort(arr, len(arr), [3, 1], 2)
    assert arr == sorted(arr)

def test_shell_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    shell_sort(arr, len(arr), [2, 1], 2)
    assert arr == [1, 2, 3, 4, 5]

def test_shell_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    shell_sort(arr, len(arr), [3, 1], 2)
    assert arr == [1, 2, 3, 4, 5]
