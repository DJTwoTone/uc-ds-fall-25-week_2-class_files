"""Optional stretch tests for in-place rotation.

These tests assume the function exists at:
    src/arrays_inplace_stretch.py -> rotate_right_inplace(nums, k)

If you don't include the stretch in your assignment, omit this file
from the autograder config so required tests still pass.
"""

import pytest
from src.arrays_inplace_stretch import rotate_right_inplace


def _rotate_and_assert(data: list[int], k: int, expected: list[int]) -> None:
    nums = list(data)
    before_id = id(nums)
    out = rotate_right_inplace(nums, k)
    # Must be in-place and return None
    assert out is None
    assert id(nums) == before_id
    assert nums == expected


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3], 0, [1, 2, 3]),                    # k = 0 (no change)
        ([1, 2], 2, [1, 2]),                          # k == n
        ([9], 100, [9]),                              # single element
        ([], 3, []),                                  # empty list
        ([10, 20, 30, 40], 102, [30, 40, 10, 20]),    # k reduced by modulo
        ([2, 2, 3, 3], 3, [2, 2, 3, 3]),              # duplicates handled
    ],
)
def test_rotate_right_inplace_cases(nums, k, expected):
    _rotate_and_assert(nums, k, expected)


def test_rotate_right_inplace_negative_k_raises():
    nums = [1, 2, 3]
    with pytest.raises(ValueError):
        rotate_right_inplace(nums, -1)


def test_rotate_right_inplace_identity_preserved():
    nums = [1, 2, 3, 4]
    ref = nums
    rotate_right_inplace(nums, 1)
    # Ensure the same object was modified
    assert ref is nums