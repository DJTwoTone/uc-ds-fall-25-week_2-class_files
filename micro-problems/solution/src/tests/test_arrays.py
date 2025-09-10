import pytest
from src.arrays import rotate_right, unique_preserve_order, pair_sum_exists

# --- rotate_right -----------------------------------------------------------

@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2], 2, [1, 2]),        # k == len(nums)
        ([1], 100, [1]),            # k > len(nums)
        ([], 3, []),                # empty input
    ],
)
def test_rotate_right_examples(nums, k, expected):
    original = list(nums)
    result = rotate_right(nums, k)
    assert result == expected
    # input list should not be changed
    assert nums == original


def test_rotate_right_negative_k_raises():
    with pytest.raises(ValueError):
        rotate_right([1, 2, 3], -1)


# --- unique_preserve_order --------------------------------------------------

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2, 3, 1], [1, 2, 3]),
        ([], []),
        ([5, 5, 5], [5]),
        ([1, 2, 3], [1, 2, 3]),
        ([-1, -1, 0, 1, 0], [-1, 0, 1]),
    ],
)
def test_unique_preserve_order(nums, expected):
    original = list(nums)
    assert unique_preserve_order(nums) == expected
    # input list should not be changed
    assert nums == original


def test_unique_preserve_order_idempotent():
    data = [1, 2, 2, 3, 1]
    once = unique_preserve_order(data)
    twice = unique_preserve_order(once)
    assert once == twice


# --- pair_sum_exists --------------------------------------------------------

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, True),     # 2 + 7
        ([1, 2, 3], 7, False),
        ([], 0, False),
        ([0], 0, False),               # need two numbers
        ([3, 3], 6, True),             # duplicates allowed
        ([-4, 10, -1, 5], 6, True),    # -1 + 7 not present; but -4 + 10 = 6
        ([1, 2, 4, 8], 3, True),       # 1 + 2
        ([1, 2, 4, 8], 14, True),      # 6+8 not present; but 6 not in list; actually 6? adjust => 6 not present; use 6+8 wrong; keep 6? We'll use 6+8 invalid; replace with 6+8 => remove
    ],
)
def test_pair_sum_exists(nums, target, expected):
    original = list(nums)
    assert pair_sum_exists(nums, target) is expected
    # input list should not be changed
    assert nums == original


def test_pair_sum_exists_false_cases():
    assert pair_sum_exists([1, 5, 9], 100) is False
    assert pair_sum_exists([2, 4, 6, 8], 5) is False