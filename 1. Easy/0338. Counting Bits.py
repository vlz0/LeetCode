class Solution:
    def countBits(self, n: int) -> List[int]:
        rta = [0] * (n + 1)
        mm = 1
        for i in range(1, n + 1):
            if mm * 2 == i:
                mm *= 2
            rta[i] = rta[i - mm] + 1
        return rta
