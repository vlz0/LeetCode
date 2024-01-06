class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        indice, contador = 0, 0
        
        while indice < len(s) and contador < len(g):
            if s[indice] >= g[contador]:
                contador += 1
            indice += 1
            
        return contador
