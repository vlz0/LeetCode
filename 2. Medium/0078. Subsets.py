class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return ayuda(0, nums, [], [])

def ayuda(i, nums, j, respuesta):
      if i == len(nums):
          if j not in respuesta:
              respuesta.append(j)
          return 
      ayuda(i + 1, nums, j + [nums[i]], respuesta)
      ayuda(i + 1, nums, j, respuesta)
      return respuesta
