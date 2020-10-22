class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    sol = Solution()
    result = sol.addDigits(38)
    print(result)
