class Solution:
    def checkRecord(self, s: str) -> bool:
        contador = 0
        for i in range(len(s)):
            if s[i] == 'A':
                contador += 1
            if contador == 2:
                return False
            if i >= 2 and s[i] == s[i - 1] == s[i - 2] == 'L':
                return False
        return True
