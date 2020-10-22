class Solution:
    def generate(self, numRows):
        ans = []

        for r in range(numRows):
            row = [None for _ in range(r + 1)]
            row[0], row[-1] = 1, 1

            for idx in range(1, len(row) - 1):
                row[idx] = ans[r - 1][idx - 1] + ans[r - 1][idx]

            ans.append(row)

        return ans


if __name__ == "__main__":
    sol = Solution()
    result = sol.generate(5)
    print(result)
