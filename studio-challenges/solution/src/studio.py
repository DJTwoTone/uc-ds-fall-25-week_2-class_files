"""Solution — Week 02 Studio Challenges.

All functions are pure and typed. Python 3.11+.
"""
from typing import List, Tuple


def detect_first_low_stock(initial: int, daily_sales: List[int], threshold: int) -> int | None:
    """Return the earliest day index where remaining stock <= threshold.

    Time: O(n) — scan once.
    Space: O(1).
    """
    remaining = initial
    for i, sold in enumerate(daily_sales):
        if sold < 0:
            raise ValueError("daily_sales cannot contain negative values")
        remaining -= sold
        if remaining <= threshold:
            return i
    return None


def has_window_with_avg_at_least(values: List[int], k: int, target_avg: float) -> bool:
    """Sliding window: any length-k window with average >= target_avg?

    Time: O(n) — each element enters/exits the window once.
    Space: O(1) — constant extra space.
    """
    n = len(values)
    if k <= 0:
        raise ValueError("k must be positive")
    if k > n:
        return False

    target_sum = target_avg * k
    window_sum = sum(values[:k])
    if window_sum >= target_sum:
        return True

    for i in range(k, n):
        window_sum += values[i] - values[i - k]
        if window_sum >= target_sum:
            return True
    return False


def merge_log_streams(a: List[Tuple[int, str]], b: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """Classic two-pointer merge for ascending timestamped records.

    Time: O(n + m) where n=len(a), m=len(b).
    Space: O(n + m) for the new combined list.
    """
    i = j = 0
    out: List[Tuple[int, str]] = []
    while i < len(a) and j < len(b):
        ta, tb = a[i][0], b[j][0]
        if ta <= tb:  # `a` wins ties
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    # append any remainder
    if i < len(a):
        out.extend(a[i:])
    if j < len(b):
        out.extend(b[j:])
    return out