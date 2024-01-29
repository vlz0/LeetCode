class Solution:
    def reverseWords(self, s: str) -> str:
        lista = s.split()
        s = ''
        for i in lista:
            s = s + ' ' + i[::-1]
        return(s[1:])
