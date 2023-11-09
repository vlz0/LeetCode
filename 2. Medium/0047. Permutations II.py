class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #return set(list(permutations(nums)))
        permutaciones = permutations(nums)
        lista = []
        for i in permutaciones:
            if i not in lista:
                lista.append(i)
        return lista
