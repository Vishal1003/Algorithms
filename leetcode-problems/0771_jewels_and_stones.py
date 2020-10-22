"""
Approach #1: Brute Force [Accepted]
- O(J.length∗S.length)), O(1)

Approach #2: Hash Set [Accepted]
- O(J.length∗S.length)), O(J.length)
"""
import collections


class Solution:
    def numJewelsInStones1(self, J, S):
        return sum(s in J for s in S)

    def numJewelsInStones2(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)

    def numJewelsInStones(self, J: str, S: str) -> int:
        d = collections.Counter(S)
        cnt = 0
        for char in J:
            if char in S:
                cnt += d[char]
        return cnt