class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return x if x < 2147483648 and x >= -2147483648 else 0

    def reverse2(self, x: int) -> int:
        ans = 0
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x != 0:
            pop = x % 10
            x //= 10
            ans = ans * 10 + pop
            # print(f"pop: {pop} x: {x} rev: {ans}")

        if -2**31 <= ans <= 2**31 - 1:
            return ans * sign
        else:
            return 0
