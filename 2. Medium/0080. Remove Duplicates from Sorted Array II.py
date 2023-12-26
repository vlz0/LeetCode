class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        indice = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[indice - 2]:
                nums[indice] = nums[i]
                indice += 1

        return indice
