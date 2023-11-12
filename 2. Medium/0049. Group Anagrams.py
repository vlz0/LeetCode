class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listado = {}
        for i in strs :
            organizado = ''.join(sorted(list(i)))
            if organizado not in listado :
                listado[organizado] = []
            listado[organizado].append(i)
        respuesta = list(listado.values())
        return respuesta
