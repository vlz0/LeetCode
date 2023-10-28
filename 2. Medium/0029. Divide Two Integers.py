class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        sign = +1 if dividend ^ divisor >= 0 else -1
        
        dividend = abs(dividend) 
        divisor = abs(divisor)
        ans = 0      
        
        for i in range(31, -1, -1) :
            if (divisor << i) <= dividend:
                ans += (1 << i)
                dividend -= (divisor << i)
           
        ans = ans * sign
        
        if not (-2**31 <= ans <= 2**31-1):
            return 2**31 - 1
        else:
            return ans
