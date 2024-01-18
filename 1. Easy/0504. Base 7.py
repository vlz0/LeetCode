class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0" 

        respuesta = ""
        n = num

        if num < 0:
            n = 0 - num
        while (n != 0):
            respuesta = str(n % 7) + respuesta
            n = n // 7
            
        return (respuesta if num > 0 else "-" + respuesta)
