class Solution:
    def isHappy(self, n: int) -> bool:
        usado = []
        while(n>0):
            respaldo = 0
            while(n > 0):
                i = n % 10
                respaldo += i * i
                n = n // 10
            if(respaldo in usado):
                return False
            else:
                usado.append(respaldo)
            if(respaldo==1):
                return True
            n = respaldo
        return False
