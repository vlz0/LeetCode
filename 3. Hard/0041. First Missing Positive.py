class Solution:
    def firstMissingPositive(self, numeros: List[int]) -> int:
        lista = set(numeros)
        i = 1
        while i in lista:
            i += 1
        return i
