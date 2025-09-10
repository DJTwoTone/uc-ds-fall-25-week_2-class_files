from typing import List




def rotate_right_inplace(nums: List[int], k: int) -> None:
    """Rotate the list to the right by k steps in place.


    Uses the three‑reversal method:
    1) reverse whole list
    2) reverse first k
    3) reverse the rest


    Time: O(n) Space: O(1)
    """
    if k < 0:
        raise ValueError("k must be non-negative")
    n = len(nums)
    if n == 0:
        return
    k %= n
    if k == 0:
        return
    


    def rev(a: List[int], i: int, j: int) -> None:
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1


    rev(nums, 0, n - 1)
    rev(nums, 0, k - 1)
    rev(nums, k, n - 1)