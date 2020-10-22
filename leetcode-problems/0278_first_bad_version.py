# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
                
            # print("mid: {} l: {} r: {}".format(mid, l, r))
        
        return l