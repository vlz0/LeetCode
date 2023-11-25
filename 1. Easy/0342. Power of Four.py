class Solution:
    def isPowerOfFour(self, n):
        for i in range(16):
            cuatro = 4 ** i
            if cuatro == n:
                return True
            if cuatro > n:
                return False
        return False
