"""
Approach 1: Brute-force [Time Limit Exceeded]

Approach 2: Greedy with Stack
- O(n), O(n)

Use Monotonic stack method:
- if newer element is less than stack.top, then remove the top element and append the new element.
"""
import re

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # Construct a monotone increasing sequence of digits
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        stack = stack[:-k] if k else stack

        # trip the leading zeros
        return "".join(stack).lstrip('0') or "0"

    def removeKdigits2(self, num: str, k: int) -> str:
        # if len(num) == k:
        #     return "0"

        stack = []
        for n in num:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)

        ans = ''.join(stack[:-k or None]).lstrip('0') or '0'
        return ans

    def removeKdigits3(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)

        # For case like 453219 or 111111.
        while k:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or '0'

    def removeKdigits4(self, num, k):
        sub = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]|7[0-6]|8[0-7]|9[0-8]|.$').sub
        for _ in range(k):
            num = sub(lambda m: m.group()[1:], num, 1)
        return num.lstrip('0') or '0'

    def removeKdigits5(self, num: str, k: int) -> str:
        if k == 0:
            return num
        while k > 0:
            k -= 1
            i = 0
            while i < len(num) - 1:
                if num[i] > num[i + 1]:  # need to remove this ith index
                    break
                i += 1
            num = num[:i] + num[i + 1:]
        if len(num) == 0:
            return "0"
        return str(int(num))


if __name__ == "__main__":
    # num = "1432219"
    num = "100"
    k = 1
    # k = 3
    sol = Solution()
    result = sol.removeKdigits2(num, k)
    print(result)