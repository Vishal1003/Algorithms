"""
Approach 1: Divide and Conquer
- O(N), O(log n)

Approach 2: Greedy
- O(N), O(1)

Approach 3: Dynamic Programming (Kadane's algorithm)
- O(N), O(1)
"""


class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray1(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def maxSubArray3(self, nums: List[int]) -> int:
        n = len(nums)
        # curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(max_sum, nums[i])

        return max_sum

    def maxSubArray_1(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        return max(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = sol.maxSubArray1(nums)
    print(result)
