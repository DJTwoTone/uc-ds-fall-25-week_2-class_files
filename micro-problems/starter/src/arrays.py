# """Starter — Week 02 micro‑problems.


# Implement the three functions below.
# Rules:
# - Keep function names and signatures the same.
# - Add type hints and docstrings (already provided).
# - Handle edge cases noted in each docstring.
# """
from typing import List
import math



# def rotate_right(nums: List[int], k: int) -> List[int]:
#     """Return a new list where the elements are rotated to the right by k steps.


#     Examples:
#     rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
#     rotate_right([1, 2], 2) -> [1, 2] # k may be >= len(nums)


#     Constraints / Edge cases:
#     - If k < 0: raise ValueError("k must be non-negative").
#     - If nums is empty, return an empty list.
#     - Function should not mutate the input list."""
    
#     if k == 0:
#         return nums
    
#     if len(nums) == 0:
#         return nums
    
#     if k < 0:
#         raise "k must be non-negative"
    
#     new_k = math.floor(k % len(nums))
    
#     front = nums[len(nums) - new_k:len(nums)]
#     back = nums[0:len(nums) - new_k]
    
#     new_list = front + back

#     return new_list

#     # raise NotImplementedError

# print(rotate_right([1, 2, 3, 4, 5], 2))
# print(rotate_right([4, 6, 2, 8, 9, 16, 72], 255))
# print(rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3])
# print(rotate_right([1, 2], 1) == [2, 1])
# print(rotate_right([1, 2], 2) == [1, 2])
# print(rotate_right([], 3) == [])
# print(rotate_right([1, 2, 3, 4, 5], -2) == "k must be non-negative")


# def unique_preserve_order(nums: List[int]) -> List[int]:
#     """Return a new list with duplicates removed, keeping first occurrences.

    
#     Example:
#     unique_preserve_order([1, 2, 2, 3, 1]) -> [1, 2, 3]


#     Constraints / Edge cases:
#     - Empty list -> empty list.
#     - All duplicates or already unique are both valid inputs.
#     - Function should not mutate the input list.
#     """

#     return [*set(nums)]

#     raise NotImplementedError

# print(unique_preserve_order([1, 2, 2, 3, 1]))


def pair_sum_exists(nums: List[int], target: int) -> bool:
    """Return True if any two numbers in nums add up to target, else False.


    Examples:
    pair_sum_exists([2, 7, 11, 15], 9) -> True # 2 + 7
    pair_sum_exists([1, 2, 3], 7) -> False


    Constraints / Edge cases:
    - Works for empty list (return False).
    - Negative numbers and repeated values are allowed.
    - Function should not mutate the input list.
    """

    if len(nums) == 0:
        return False
    
    for i, x in enumerate(nums):
        new_list = nums[i - len(nums):len(nums)]
        for y in new_list:
            if x + y == target:
                return True
    return False
    # raise NotImplementedError

print(pair_sum_exists([2, 7, 11, 15], 9) == True)
print(pair_sum_exists([1, 2, 3], 7) == False)