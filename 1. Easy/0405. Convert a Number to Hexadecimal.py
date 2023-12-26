class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hexa = "0123456789abcdef"
        ans = ""
        while num != 0 and len(ans) < 8:
            ans = hexa[num & 15] + ans
            num >>= 4
        return ans
