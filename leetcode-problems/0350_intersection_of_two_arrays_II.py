"""
Approach 1: Hash Map
- O(m + n), O(min(m, n))

Approach 2: Sort
- O(n log(n) + m log(m)), O(1)

"""
class Solution:
    def intersect(self, nums1, nums2):
        intersection_list = []
        if len(nums1) >= len(nums2):
            for n in nums2:
                if n in nums1:
                    index = nums1.index(n)
                    nums1.pop(index)
                    intersection_list.append(n)

        else:
            for n in nums1:
                if n in nums2:
                    index = nums2.index(n)
                    nums2.pop(index)
                    intersection_list.append(n)
        return intersection_list


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = sol.intersect(nums1, nums2)
    print(result)
