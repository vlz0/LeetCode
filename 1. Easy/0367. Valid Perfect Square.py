class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        izq = 0
        der = num

        while izq <= der:
            mitad = izq + (der - izq) // 2

            if mitad * mitad == num:
                return True
            elif mitad * mitad > num:
                der = mitad - 1  
            else:
                izq = mitad + 1
