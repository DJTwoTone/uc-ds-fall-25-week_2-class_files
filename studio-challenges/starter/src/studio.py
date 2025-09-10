"""Starter — Week 02 Studio Challenges.

Implement the three functions below. Keep names/signatures the same.
Add type hints and docstrings (already provided). Do not mutate inputs.
"""

from typing import List, Tuple


def detect_first_low_stock(initial: int, daily_sales: List[int], threshold: int) -> int | None:
    """Return the first day index when remaining stock <= threshold, else None.

    Word problem:
        A shop starts with `initial` items. After each day i, it sells
        `daily_sales[i]` items. Report the earliest day when the remaining
        stock is at or below the warning `threshold`. If it never happens,
        return None.

    Notes / Constraints:
        - Count after each day is applied (end-of-day check).
        - `daily_sales` must not contain negatives. If it does, raise ValueError.
        - If `daily_sales` is empty, return None.

    Examples:
        initial=10, sales=[2,2,3,1], threshold=3 -> day 2 (remaining 3)
        initial=5,  sales=[1,1,1],   threshold=10 -> None
    """
    raise NotImplementedError


def has_window_with_avg_at_least(values: List[int], k: int, target_avg: float) -> bool:
    """Return True if any consecutive window of size k has average >= target_avg.

    Word problem:
        A health app records steps per day. Did the user hit their goal on
        any stretch of k days on average? (e.g., any 7-day window averaging
        at least 8,000 steps.)

    Notes / Constraints:
        - If k <= 0: raise ValueError.
        - If k > len(values): return False.
        - Works with zeros/negatives.

    Examples:
        values=[1, 9, 10, 2, 1], k=3, target_avg=5.0 -> True (1+9+10)/3
        values=[2, 2], k=3, target_avg=2.0 -> False
    """
    raise NotImplementedError


def merge_log_streams(a: List[Tuple[int, str]], b: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """Merge two ascending-by-time streams into one ascending list.

    Word problem:
        Two servers write logs: (timestamp, message). Each list `a` and `b`
        is already sorted by timestamp (ascending). Create one combined list
        that preserves the sorted order. If timestamps tie, take from `a`
        first, then `b` (stable merge).

    Notes / Constraints:
        - Do not modify inputs.
        - Assume timestamps are ints; messages are short strings.

    Examples:
        a=[(1, 'A1'), (3,'A3')], b=[(2,'B2'), (3,'B3')] ->
        [(1,'A1'), (2,'B2'), (3,'A3'), (3,'B3')]
    """
    raise NotImplementedError