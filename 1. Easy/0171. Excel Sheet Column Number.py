class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cnt=0
        for i in range(len(columnTitle)):
            cnt+=(26**(len(columnTitle)-i-1))*(ord(columnTitle[i])-64)
        return cnt
