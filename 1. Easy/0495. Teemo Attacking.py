class Solution:
    def findPoisonedDuration(self, tiempo: List[int], duration: int) -> int:
        resultado = 0
        for i in range(len(tiempo) - 1):
            resultado += min(tiempo[i + 1] - tiempo[i], duration)
        return resultado + duration
