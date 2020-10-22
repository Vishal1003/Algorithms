"""
Approach 1: Schoolbook Addition with Carry
- T: O(n), S: O(n) {O(1): when digits contains at least one not-nine digit}
"""
class Solution:
    # approach-1
    def plusOne1(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits

    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]


if __name__ == "__main__":
    sol = Solution()
    digits = [4, 3, 2, 1]
    result = sol.plusOne(digits)
    print(result)
