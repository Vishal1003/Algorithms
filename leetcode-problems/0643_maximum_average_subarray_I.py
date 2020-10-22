"""
Pattern: Sliding Window
Approach 1: Brute Force: O(N * k) Time Limit Exceed

Approach 2: update window sum.
- O(n), O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = sum(nums[0:k])
        max_sum = _sum

        for i in range(len(nums) - k):
            _sum += nums[i + k] - nums[i]
            max_sum = max(max_sum, _sum)

        return max_sum / k

    def findMaxAverage1(self, nums: List[int], k: int) -> float:
        _sum = sum(nums[0:k])
        max_sum = _sum

        for i in range(k, len(nums)):
            _sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, _sum)

        max_avg = max_sum / k
        return max_avg