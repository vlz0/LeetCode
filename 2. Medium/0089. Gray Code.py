class Solution:
    def grayCode(self, n: int) -> List[int]:
        respuesta = [0, 1]
        for i in range(1, n):
            x = 1 << i
            for i in range(len(respuesta) - 1, -1, -1):
                respuesta.append(respuesta[i] | x)
        return respuesta
