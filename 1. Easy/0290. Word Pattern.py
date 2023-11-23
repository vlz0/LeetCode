class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")
        if len(pattern) != len(l):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(l)):
            if pattern[i] in d1 and d1[pattern[i]] != l[i]:
                return False
            if l[i] in d2 and d2[l[i]] != pattern[i]:
                return False
            d1[pattern[i]] = l[i]
            d2[l[i]] = pattern[i]
            
        return True
