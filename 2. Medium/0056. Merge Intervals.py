class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        listado = [intervals[0]]
        for i in intervals:
            mm = listado[-1]
            if i[0] <= mm[1]:
                listado[-1] = [min(mm[0], i[0]), max(mm[1], i[1])]
            else:
                listado.append(i)
        return listado
