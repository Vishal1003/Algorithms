"""
Approach 1: Left-to-Right Pass: T: O(1), S: O(1)
Approach 2: Left-to-Right Pass Improved: T: O(1), S: O(1)
Approach 3: Right-to-Left Pass

"""
# approach - 1
values1 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

# approach - 2
values2 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


class Solution:
    # approach 1
    def romanToInt1(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values1[s[i]] < values1[s[i + 1]]:
                total += values1[s[i + 1]] - values1[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values1[s[i]]
                i += 1
        return total

    # approach - 2
    def romanToInt2(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i < len(s) - 1 and s[i:i + 2] in values2:
                total += values2[s[i:i + 2]]
                i += 2
            else:
                total += values2[s[i]]
                i += 1
        return total

    # approach - 3
    def romanToInt(self, s: str) -> int:
        total = values1.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values1[s[i]] < values1[s[i + 1]]:
                total -= values1[s[i]]
            else:
                total += values1[s[i]]
        return total

    def romanToInt4(self, s: str) -> int:
        roman_value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        subtraction_dict = {'IV': 4, 'IX': 9,
                            'XL': 40, 'XC': 90,
                            'CD': 400, 'CM': 900}
        int_value = 0
        for k, v in subtraction_dict.items():
            while k in s:
                s_index = s.find(k)
                s = s[:s_index] + s[s_index + 2:]
                int_value = int_value + v
                # print(s)

        for char in s:
            int_value = int_value + roman_value_dict[char]

        return int_value
