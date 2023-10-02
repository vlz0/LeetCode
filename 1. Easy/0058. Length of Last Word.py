class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        frase = s.split()
        return len(frase[-1])
