class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 -1
        INT_MIN = -2**31

        n = len(s)
        i = 0

        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+': 
            i += 1
        
        res = 0 
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            res = res * 10 + digit
            i += 1
        res = sign * res
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        
        return res
