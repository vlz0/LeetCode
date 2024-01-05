class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numeros = set(nums)
        faltan = []

        for i in range(1, len(nums) + 1):
            if i not in numeros:
                faltan.append(i)

        return faltan
