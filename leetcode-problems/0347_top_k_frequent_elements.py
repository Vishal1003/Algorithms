import collections


class Solution:
    def topKFrequent(self, nums, k):
        l = list(collections.Counter(nums).items())
        l_sorted = [i for i, _ in sorted(l, key=lambda x: x[1], reverse=True)]
        return l_sorted[:k]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = sol.topKFrequent(nums, k)
    print(result)
