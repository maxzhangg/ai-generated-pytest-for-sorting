 
import pytest
from sorting_algorithms.radix_sort import radixSort

def test_radix_sort_basic():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)
    assert arr == sorted(arr)

def test_radix_sort_empty():
    arr = []
    radixSort(arr)
    assert arr == []

def test_radix_sort_single():
    arr = [5]
    radixSort(arr)
    assert arr == [5]

def test_radix_sort_duplicates():
    arr = [5, 3, 5, 3, 2]
    radixSort(arr)
    assert arr == sorted(arr)

def test_radix_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    radixSort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_radix_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    radixSort(arr)
    assert arr == [1, 2, 3, 4, 5]
import pytest
from sorting_algorithms.radix_sort import radixSort

def test_radix_sort_basic():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)
    assert arr == sorted(arr)

def test_radix_sort_empty():
    arr = []
    radixSort(arr)
    assert arr == []

def test_radix_sort_single():
    arr = [5]
    radixSort(arr)
    assert arr == [5]

def test_radix_sort_duplicates():
    arr = [5, 3, 5, 3, 2]
    radixSort(arr)
    assert arr == sorted(arr)

def test_radix_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    radixSort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_radix_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    radixSort(arr)
    assert arr == [1, 2, 3, 4, 5]
