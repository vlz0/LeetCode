class Solution:
    def moveZeroes(self, nums: List[int]) -> None:        
        """
        Do not return anything, modify nums in-place instead.
        """
        indice = 0

        for i in nums:
            if i != 0:
                nums[indice] = i
                indice += 1

        while indice < len(nums):
            nums[indice] = 0
            indice += 1
