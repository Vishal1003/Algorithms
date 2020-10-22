import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for idx, char in enumerate(s):
            if d[char] == 1:
                return idx
        return -1

if __name__ == "__main__":
    sol = Solution()
    s = 'leetcode'
    result = sol.firstUniqChar(s)
    print(result)
