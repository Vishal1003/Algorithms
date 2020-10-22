class Solution:
    def reformat(self, s):
        if s.isalpha():
            if len(s) is 1:
                return s
            else:
                return ""
        elif s.isdigit():
            if len(s) is 1:
                return s
            else:
                return ""
        else:
            digits = []
            alphs = []
            for char in s:
                if char.isalpha():
                    alphs.append(char)
                elif char.isdigit():
                    digits.append(char)
            
            total_alphs = len(alphs)
            total_digits = len(digits)
            ans = []
            cnt = 0 if total_alphs >= total_digits else 1
            
            if total_alphs == total_digits or total_alphs == total_digits + 1 or total_alphs == total_digits - 1:
                while total_alphs != 0 and total_digits !=0:
                    if cnt % 2 is 0 and alphs:
                        ans.append(alphs.pop(0))
                        cnt += 1
                    elif digits:
                        ans.append(digits.pop(0))
                        cnt += 1
                    else:
                        if len(alphs) == 0 and len(digits) == 0:
                            return "".join(ans)
            else:
                return ""
