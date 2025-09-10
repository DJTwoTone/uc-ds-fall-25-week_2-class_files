import pytest
from src.studio import detect_first_low_stock, has_window_with_avg_at_least, merge_log_streams

# --- detect_first_low_stock -------------------------------------------------

@pytest.mark.parametrize(
    "initial,sales,threshold,expected",
    [
        (10, [2, 2, 3, 1], 3, 2),      # 10-2-2-3=3 at day 2
        (5, [1, 1, 1], 10, None),      # never dips that low
        (8, [0, 0, 0], 7, 0),          # hits at day 0 after first day
        (3, [], 2, None),              # no days -> no check
    ],
)
def test_detect_first_low_stock_basic(initial, sales, threshold, expected):
    original = list(sales)
    assert detect_first_low_stock(initial, sales, threshold) == expected
    assert sales == original  # input not mutated


def test_detect_first_low_stock_negative_sales_raises():
    with pytest.raises(ValueError):
        detect_first_low_stock(10, [1, -2, 3], 5)


# --- has_window_with_avg_at_least ------------------------------------------

@pytest.mark.parametrize(
    "values,k,target,expected",
    [
        ([1, 9, 10, 2, 1], 3, 5.0, True),   # 1+9+10=20 -> avg 6.67
        ([2, 2], 3, 2.0, False),            # k > n
        ([5, 5, 5, 5], 2, 5.0, True),       # exactly meets target
        ([0, 0, 0, 0], 2, 0.1, False),      # never reaches
        ([-1, 9, -1, 9], 2, 4.0, True),     # negatives allowed
    ],
)
def test_has_window_with_avg_at_least(values, k, target, expected):
    original = list(values)
    assert has_window_with_avg_at_least(values, k, target) is expected
    assert values == original


def test_has_window_with_avg_at_least_bad_k():
    with pytest.raises(ValueError):
        has_window_with_avg_at_least([1, 2, 3], 0, 1.0)


# --- merge_log_streams ------------------------------------------------------

def test_merge_basic():
    a = [(1, "A1"), (3, "A3"), (5, "A5")]
    b = [(2, "B2"), (3, "B3"), (4, "B4")]
    merged = merge_log_streams(a, b)
    assert merged == [
        (1, "A1"), (2, "B2"), (3, "A3"), (3, "B3"), (4, "B4"), (5, "A5")
    ]
    # inputs unchanged
    assert a == [(1, "A1"), (3, "A3"), (5, "A5")]
    assert b == [(2, "B2"), (3, "B3"), (4, "B4")]


def test_merge_one_empty():
    assert merge_log_streams([], [(1, "x")]) == [(1, "x")]
    assert merge_log_streams([(1, "x")], []) == [(1, "x")]


def test_merge_ties_from_a_first():
    a = [(1, "A1"), (2, "A2")]
    b = [(1, "B1"), (2, "B2")]
    assert merge_log_streams(a, b) == [
        (1, "A1"), (1, "B1"), (2, "A2"), (2, "B2")
    ]