class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curr_min, curr_max = 0, 0
        min_sum, max_sum = float('inf'), -float('inf')
        total_sum = 0

        for item in A:
            curr_min = min(curr_min + item, item)
            curr_max = max(curr_max + item, item)

            min_sum = min(min_sum, curr_min)
            max_sum = max(max_sum, curr_max)
            total_sum += item

        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum