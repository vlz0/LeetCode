class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        contador = 0 
        maximo = 0 
        for i in nums:
            if i != 1 :
                maximo = max(maximo , contador)
                contador = 0 
            else:
                contador += 1 
        return max(maximo , contador) 
