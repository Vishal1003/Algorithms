class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1


if __name__ == "__main__":
    sol = Solution()
    num = [0, 1, 0, 3, 12]
    result = sol.moveZeroes(num)
    print(result)
