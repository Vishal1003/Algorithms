class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        table = {0: 0}
        for idx, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_len = max(max_len, idx - table[count])
            else:
                table[count] = idx
        
        return max_len