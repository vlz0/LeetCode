class Solution:
    def reverseVowels(self, s: str) -> str:
        vocales = ['a', 'e', 'i', 'o','u','A','E','I','O','U']
        i = 0
        j  =len(s) - 1
        s = list(s)
        while(i < j):
            if s[i] not in vocales:
                i += 1
            if s[j] not in vocales:
                j -= 1
            if s[i] in vocales and s[j] in vocales:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        s = "".join(s)
        return s
