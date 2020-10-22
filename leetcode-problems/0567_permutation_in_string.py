class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1, ns2 = len(s1), len(s2)
        s1_cnt, s2_window = collections.Counter(s1), collections.Counter(s2[0:ns1])

        # check for first substring of s2. If same, then return True
        if s2_window == s1_cnt:
            return True

        for idx in range(ns1, ns2):
            """
            c1 - last element of current window --> increment count
            c2 - first element of previous window --> decrement count
            """
            c1, c2 = s2[idx], s2[idx - ns1]
            # setdefault -> if key is not present in dictionary then assign 0 as default value
            s2_window[c1] = s2_window.setdefault(c1, 0) + 1
            if s2_window[c2] > 1:
                s2_window[c2] = s2_window.setdefault(c2, 0) - 1
            else:
                del s2_window[c2]

            if s2_window == s1_cnt:
                return True
        return False

