class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = None
        cu = 0
        for num in nums:
            if cu == 0:
                c = num
                cu = 1
            elif num == c:
                cu += 1
            else:
                cu -= 1
        cu_c = nums.count(c)
        if cu_c > len(nums) // 2:
            return c
