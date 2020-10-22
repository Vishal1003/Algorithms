class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = sol.intersection(nums1, nums2)
    print(result)
