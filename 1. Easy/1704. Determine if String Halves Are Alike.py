class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, 0

        hal_l = len(s) // 2

        for l, r in zip(s[:hal_l], s[hal_l:]):
            if l in vocales: 
                left += 1
            if r in vocales: 
                right += 1

        return left == right
