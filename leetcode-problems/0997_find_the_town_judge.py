"""
Approach 1: Two Arrays
- O(edges), O(n)

Approach 2: One Array
- O(edges), O(n)
"""
class Solution:
    def findJudge1(self, N: int, trust: List[List[int]]) -> int:

        if len(trust) < N - 1:
            return -1

        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1

    def findJudge2(self, N: int, trust: List[List[int]]) -> int:

        if len(trust) < N - 1:
            return -1

        trust_scores = [0] * (N + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for i, score in enumerate(trust_scores[1:], 1):
            if score == N - 1:
                return i
        return -1

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        votes = [-1] + [0] * N
        for a, b in trust:
            # a loses his chance of being the judge
            votes[a] = float('-inf')
            votes[b] += 1
        for i, v in enumerate(votes):
            # check if there is anyone got all other people's votes.
            if v == N-1: return i
        return -1