class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
            
        mmm = set()
        for i in range(len(nums)):
            if nums[i] in mmm:
                return True
            mmm.add(nums[i])
            if len(mmm)==k + 1:
                mmm.remove(nums[i - k])
        return False
