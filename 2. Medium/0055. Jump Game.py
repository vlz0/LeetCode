class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mm = len(nums)-1

        while mm > 0:
            if nums[mm - 1] > 0:
                mm -= 1
            else:
                i = mm - 1
                while nums[i] < mm - i:
                    if i <= 0:
                        return False
                    i -= 1
                mm = i
        return True
