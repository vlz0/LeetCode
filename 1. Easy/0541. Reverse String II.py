class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lista = list(s)
        largo = len(s)
        i = 0
        while i < largo:
            if (i + k) <= largo:
                lista[i:i + k] = lista[i:i + k][::-1]
            else:
                lista[i:] = lista[i:][::-1]
            i += 2 * k
        return ''.join(lista)
