"""
Approach 1: Built-in BitCounting Functions
- O(1), O(1)

Approach 2: Bit Shift
- O(1), O(1)

Approach 3: Brian Kernighan's Algorithm
- O(1), O(1)
"""
class Solution:
    def hammingDistance1(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance

    def hammingDistance3(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance