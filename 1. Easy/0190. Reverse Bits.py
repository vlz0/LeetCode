class Solution:
    def ayuda(self, n, r, count):
        if n < 1:
            return r << (32 - count)
        return self.ayuda(n >> 1, (r << 1) | (n & 1), count + 1)
    def reverseBits(self, n: int) -> int:
        return self.ayuda(n, 0, 0)
