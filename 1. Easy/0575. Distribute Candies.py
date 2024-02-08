class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType) // 2
        LEN = len(set(candyType))
        return min(n, LEN)
