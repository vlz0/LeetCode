class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        lastBucket = 0 
        
        if goal == 0:
            for num in nums:
                if num == 0:
                    lastBucket += 1
                    ans += lastBucket
                else:
                    lastBucket = 0
            return ans

        left = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            if total == goal:
                lastBucket = 0

            while total == goal:
                ans += 1
                lastBucket += 1
                total -= nums[left]
                left += 1

            if lastBucket != 0 and nums[right] == 0:
                ans += lastBucket
                
        return ans
