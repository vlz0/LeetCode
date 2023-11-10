class Solution:
    def addDigits(self, numero: int) -> int:
        if numero == 0:
            return 0
        return 1 + (numero - 1) % 9
