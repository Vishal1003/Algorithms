import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = collections.Counter(s)
        t1 = collections.Counter(t)

        for char in s1:
            if t1[char] != s1[char]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    result = sol.isAnagram(s, t)
    print(result)
