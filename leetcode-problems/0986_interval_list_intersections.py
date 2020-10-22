class Solution:
    def intervalIntersection(self, A, B):
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            lo, hi = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
