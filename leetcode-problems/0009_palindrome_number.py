class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        rev = 0
        while x > 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        return x_copy == rev


if __name__ == "__main__":
    sol = Solution()
    result = sol.isPalindrome(121)
    print(result)
