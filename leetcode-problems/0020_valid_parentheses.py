class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }   
        stack = []
        for char in s:
            if not char in map_dict:
                stack.append(char)
            else:
                top = stack.pop() if stack else '#'
                if map_dict[char] != top:
                    return False
            
        return not stack
            
            