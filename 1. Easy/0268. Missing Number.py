class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumatoria = int(n*(n+1)/2)
        apoyo = 0
        for i in nums:
            apoyo += i
        falta = sumatoria - apoyo
        return falta
