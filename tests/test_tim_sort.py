import pytest
from sorting_algorithms.timsort import tim_sort

@pytest.mark.parametrize("arr", [
    [5, 21, 7, 23, 19],
    [],
    [42],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 3, 5, 3, 2],
    [100, 20, 30, 20, 100, 10, 50],
    [0] * 100,
    list(range(1000, 0, -1)),  # Large reverse
    list(range(1000))          # Already sorted
])
def test_tim_sort_correctness(arr):
    expected = sorted(arr[:])  # Make a copy and sort
    tim_sort(arr, len(arr))
    assert arr == expected

