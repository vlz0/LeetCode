class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arreglo = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0 :
                arreglo.append("FizzBuzz")
            elif i % 3==0:
                arreglo.append("Fizz")
            elif i % 5==0 :
                arreglo.append("Buzz")
            else:
                arreglo.append(str(i))
        return(arreglo)
