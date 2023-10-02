class Solution:
    def reverse(self, x: int) -> int:

        stringMaximo =  '2147483647'

        listaRespuesta = reversed(str(abs(x)))
      
        respuesta = ''.join(listaRespuesta).rjust(10,'0')

        if respuesta > stringMaximo: return 0
       
        return int(respuesta)*(1 - 2*(x < 0))
