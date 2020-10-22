import collections


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = sol.majorityElement(nums)
    print(result)
