class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultado = []
        
        def recursion(tar,lis,ind):
            if (tar == target):
                resultado.append(lis.copy())
                return
            
            if (tar > target):
                return
            for i in range(ind, len(nums)):
                lis.append(nums[i])
                recursion(tar + nums[i], lis, i)
                lis.pop()
        recursion(0, [], 0)
        return resultado
