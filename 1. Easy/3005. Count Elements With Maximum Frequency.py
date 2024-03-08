class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = Counter(nums)
        m = max(d.values())
        return m * sum(i == m for i in d.values())
