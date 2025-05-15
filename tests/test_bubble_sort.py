import pytest

from sorting_algorithms.bubblesort import bubble_sort 


def test_empty_list():
    lista = []
    bubble_sort(lista, len(lista))
    assert lista == []

def test_sorted_list():
    lista = [1, 2, 3, 4, 5]
    bubble_sort(lista, len(lista))
    assert lista == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    lista = [5, 4, 3, 2, 1]
    bubble_sort(lista, len(lista))
    assert lista == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    lista = [3, 1, 2, 1, 4, 3]
    bubble_sort(lista, len(lista))
    assert lista == [1, 1, 2, 3, 3, 4]

def test_list_with_negative_numbers():
    lista = [-1, 2, 0, -3, 5]
    bubble_sort(lista, len(lista))
    assert lista == [-3, -1, 0, 2, 5]
