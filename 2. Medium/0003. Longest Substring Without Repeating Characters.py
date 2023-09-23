lass Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mmm = {}
        largo = 0
        for i in range(len(s)):
            if s[i] in mmm:
                if mmm[s[i]] + 1 > l: 
                    l = mmm[s[i]] + 1
            mmm[s[i]] = i 
            largo = max(largo, i - l + 1)
        return largo
