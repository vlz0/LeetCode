class Solution(object):
    def findWords(self, words):
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        respuesta = []
        for i in words:
            wordset = set(i.lower())
            if (wordset & set1 == wordset) or (wordset & set2 == wordset) or (wordset & set3 == wordset):
                respuesta.append(i)
        return respuesta
