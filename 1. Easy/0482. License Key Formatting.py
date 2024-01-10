class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        nueva = ''
        caract = k

        for i in range(len(s) - 1, -1, -1):
            if k != 0:
                nueva = s[i] + nueva
                k -= 1
            if k == 0 and i != 0:
                nueva = '-' + nueva
                k = caract

        return nueva
