class Solution:
    def jump(self, nums: List[int]) -> int:
        resutlado = 0
        izq, der = 0, 0
        while der < len(nums) - 1 :
            lejos = 0
            for i in range(izq, der + 1):
                lejos = max(lejos, i + nums[i])
            izq = der + 1
            der = lejos
            resutlado += 1
        return resutlado
