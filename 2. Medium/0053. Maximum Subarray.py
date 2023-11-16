class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximo = nums[0]
        ayuda =0
        for i in range(0, len(nums)):
            ayuda += nums[i]
            if(ayuda > maximo):
                maximo = ayuda
            if(ayuda < 0):
                ayuda = 0
        return maximo
