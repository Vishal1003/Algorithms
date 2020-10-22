"""
Approach 1: Brute Force
- O(n), O(1)

Approach 2: Binary Search
- O(log n), O(1)

Approach 3: Binary Search on Evens Indexes Only
- O(log n), O(1)
"""
class Solution:
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

    def singleNonDuplicate2(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]

    def singleNonDuplicate3(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]

    # O(n log(n))
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] ^ nums[1]

        return self.singleNonDuplicate(nums[0:len(nums) // 2]) ^ self.singleNonDuplicate(nums[len(nums) // 2:])

    # odd ^ 1 = odd - 1
    # even ^ 1 = even + 1
    def singleNonDuplicate_1(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == '__main__':
    soln = Solution()
    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums = [3, 3, 7, 7, 10, 11, 11]
    ans = soln.singleNonDuplicate(nums)
    print(ans)
