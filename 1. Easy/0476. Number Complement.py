class Solution:
    def findComplement(self, num: int) -> int:
        complemento = ''
        
        while num > 0 :
            if num % 2 == 1:
                complemento += '0'
            else:
                complemento += '1'
            num //= 2

        return int(complemento[::-1], 2)
