# pytest template showing common edge cases
import pytest

# Example: rotation edge cases (adapt for your own functions)
from src.arrays import rotate_right

@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([], 3, []),          # empty
        ([1], 0, [1]),        # single element
        ([1,2,3], 3, [1,2,3]),# k == n
        ([1,2,3], 5, [2,3,1]),# k > n
    ],
)
def test_rotation_edge_cases(nums, k, expected):
    assert rotate_right(nums, k) == expected