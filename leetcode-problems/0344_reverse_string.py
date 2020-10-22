class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s


if __name__ == "__main__":
    sol = Solution()
    s = ["H", "a", "n", "n", "a", "h"]
    result = sol.reverseString(s)
    print(result)
