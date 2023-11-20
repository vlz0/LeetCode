# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution(object):
    def firstBadVersion(self, n):
        izq = 1
        der = n

        while izq < der:
            mitad = izq + (der - izq) // 2
            if isBadVersion(mitad):
                der = mitad
            else:
                izq = mitad + 1

        return izq
