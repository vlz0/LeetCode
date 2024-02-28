class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        result = left = 0
        for right, number in enumerate(nums):
            while left < right and nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                result = max(result, right - left + 1)
        return result
