class Solution:
    def fib(self, n: int) -> int:
        fibo = [0,1]
        if n <= 1 :
            return n
        for i in range(2, n + 1 ):
            fibo.append(fibo[i - 1] + fibo[i - 2])
        return fibo[-1]        
