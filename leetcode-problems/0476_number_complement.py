"""
- O(1), O(1)
Approach 1: Flip Bit by Bit

Approach 2: Compute Bit Length and Construct 1-bits Bitmask

Approach 3: Built-in Functions to Construct 1-bits Bitmask

Approach 4: highestOneBit OpenJDK algorithm from Hacker's Delight

"""
from math import log2, floor


class Solution:
    def findComplement1(self, num):
        todo, bit = num, 1
        while todo:
            # flip current bit
            num = num ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return num

    def findComplement(self, num):
        # n is a length of num in binary representation
        n = floor(log2(num)) + 1
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # flip all bits
        return bitmask ^ num

    def findComplement3(self, num):
        return (1 << num.bit_length()) - 1 - num

    def findComplement4(self, num):
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        # flip all bits
        return bitmask ^ num

    def findComplement(self, num: int) -> int:
        """
        ex. 5 = 101 ---> complement = 2 (010)
        101 ^ 111 = 010. Here, 111(7 in decimal) = 2**(no of digits) - 1
        """
        return num ^ (pow(2, num.bit_length()) - 1)