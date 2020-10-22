"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Input: nums = [1,1,1,1,1], k = 0
Output: true
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count_zero = 0
        
        for i, n in enumerate(nums):
            if n == 1:
                if i != 0 and count_zero < k:
                    return False
                count_zero = 0
            elif n == 0:
                count_zero += 1
            
            if i == len(nums) - 1:
                return True