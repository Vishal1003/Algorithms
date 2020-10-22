"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    # Time: O(n^2), Space: O(n)??
    def two_sum_brute_force(self, nums, target):
        return [[i, j] for i in range(len(nums)) for j in range(i+1, len(nums), 1) if nums[i] + nums[j] == target][0]

    # Time: O(n), Space: O(n)
    def two_sum_hash(self, nums, target):
        d = {}
        for index, num in enumerate(nums):
            if d.get(num) is None:
                d[target - num] = index
            else:
                return [d.get(num), index]
        return -1, -1


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    res1 = Solution().two_sum_brute_force(nums, target)
    res2 = Solution().two_sum_hash(nums, target)

    print(res1, res2)
