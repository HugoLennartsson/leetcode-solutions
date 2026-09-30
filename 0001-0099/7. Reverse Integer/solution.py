import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 -1 
        MIN_INT = -2**31

        rev = 0
        while x != 0:
            pop = math.fmod(x,10)
            pop = int(pop)
            x = int(x / 10)

            if rev > MAX_INT // 10 or (rev == MAX_INT // 10 and pop > 7):
                return 0
            if rev < math.ceil(MIN_INT / 10) or (rev == math.ceil(MIN_INT / 10) and pop < -8):
                return 0 
            
            rev = rev * 10 + pop
        
        return rev