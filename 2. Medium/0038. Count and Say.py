def countAndSay(self, n: int) -> str:
    if n == 1:
        return "1"
    
    anterior = self.countAndSay(n - 1)
    n = len(prev)
    resultado = ""
    contador = 1
    
    for i in range(n):
        if (i == (n - 1)) or (anterior[i] != anterior[i + 1]):
            resultado += str(contador) + anterior[i]
            contador = 1
        else:
            contador += 1
    
    return resultado
