
# tests/test_heap_sort.py

import pytest
from sorting_algorithms.heap_sort import heapSort  

def test_heap_sort():
    # 测试普通数组
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    assert arr == [5, 6, 7, 11, 12, 13]

    # 测试空数组
    arr = []
    heapSort(arr)
    assert arr == []

    # 测试单元素数组
    arr = [1]
    heapSort(arr)
    assert arr == [1]

    # 测试包含重复元素的数组
    arr = [5, 1, 5, 3, 5, 3]
    heapSort(arr)
    assert arr == [1, 3, 3, 5, 5, 5]

    # 测试已经排序的数组
    arr = [1, 2, 3, 4, 5]
    heapSort(arr)
    assert arr == [1, 2, 3, 4, 5]

    # 测试降序数组
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapSort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

