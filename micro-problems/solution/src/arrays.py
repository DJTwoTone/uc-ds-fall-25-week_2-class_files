"""Solution — Week 02 micro‑problems.


Python 3.11+, standard library only.
Functions are pure (no mutation of inputs) and typed.
"""
from typing import List




def rotate_right(nums: List[int], k: int) -> List[int]:
    """Rotate the list right by k and return a new list.


    Time: O(n) — we copy at most n elements.
    Space: O(n) — returns a new list (not in‑place).
    """
    if k < 0:
        raise ValueError("k must be non-negative")
    n = len(nums)
    if n == 0:
        return []
    k %= n
    return nums[-k:] + nums[:-k] if k else nums[:]




def unique_preserve_order(nums: List[int]) -> List[int]:
    """Remove duplicates while keeping the first time we saw each value.


    Time: O(n) average (hash set membership).
    Space: O(n) for the `seen` set and output list.
    """
    seen: set[int] = set()
    out: List[int] = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out




def pair_sum_exists(nums: List[int], target: int) -> bool:
    """Return True if any two numbers add up to `target`.


    Time: O(n) average.
    Space: O(n) for the complement set.
    """
    need: set[int] = set()
    for x in nums:
        if x in need:
            return True
        need.add(target - x)
    return False