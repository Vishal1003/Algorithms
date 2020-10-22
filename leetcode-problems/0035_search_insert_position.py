"""
Approach 1: Binary Search

"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if target < nums[mid]:
                r = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                l = mid + 1
            
            # print("mid: {} l: {} r: {}".format(mid, l, r))
        return l