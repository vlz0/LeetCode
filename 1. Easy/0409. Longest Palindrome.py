class Solution:
    def longestPalindrome(self, s: str) -> int:
        arreglo = [x for x in s]
        frecuencia = Counter(arreglo)
        contador = list(frecuencia.values())
        resultado = 0

        for i in range(len(contador)):
            if contador[i] % 2 == 0:
                resultado += contador[i]
            else:
                resultado += contador[i] - 1

        if len(arreglo) == resultado:
            return resultado
        else:
            return resultado + 1
