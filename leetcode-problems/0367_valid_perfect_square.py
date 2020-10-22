"""
Square root related problems usually could be solved in logarithmic time.
There are three standard logarithmic time approaches, listed here from the worst to the best:
Recursion. The slowest one.
Binary Search. The simplest one.
Newton's Method. The fastest one, and therefore widely used in dynamical simulations.

Approach 1: Binary Search
- O(log N), O(1)

Approach 2: Newton's Method
- O(log N), O(1)
"""


class Solution:
    def isPerfectSquare1(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1

        return False

    def isPerfectSquare2(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            # print("mid: {} l: {} r: {}".format(mid, l, r))
        return False
