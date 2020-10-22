"""
- O(1), O(1)
Approach 1: Flip Bit by Bit

Approach 2: Compute Bit Length and Construct 1-bits Bitmask

Approach 3: Built-in Functions to Construct 1-bits Bitmask

Approach 4: highestOneBit OpenJDK algorithm from Hacker's Delight

"""
from math import log2, floor

class Solution:
    def bitwiseComplement1(self, N: int) -> int:
        if N == 0:
            return 1
        todo, bit = N, 1
        while todo:
            # flip current bit
            N = N ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return N

    def bitwiseComplement2(self, N: int) -> int:
        if N == 0:
            return 1
        # l is a length of N in binary representation
        l = floor(log2(N)) + 1
        # bitmask has the same length as N and contains only ones 1...1
        bitmask = (1 << l) - 1
        # flip all bits
        return bitmask ^ N

    def bitwiseComplement3(self, N: int) -> int:
        return (1 << N.bit_length()) - 1 - N if N else 1

    def bitwiseComplement4(self, N: int) -> int:
        if N == 0:
            return 1
        # bitmask has the same length as N and contains only ones 1...1
        bitmask = N
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        # flip all bits
        return bitmask ^ N

    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        else:return N ^ (2 ** N.bit_length() - 1)