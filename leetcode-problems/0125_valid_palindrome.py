"""
Approach 1: Compare with Reverse
- O(n), O(n)

Approach 2: Two Pointers
- O(n), O(1)
"""


class Solution:
    def isPalindrome1(self, s: str) -> bool:

        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list

    def isPalindrome2(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            mod_s = (''.join(e for e in s if e.isalnum())).lower()
            rev_s = mod_s[::-1]
        return True if mod_s == rev_s else False
