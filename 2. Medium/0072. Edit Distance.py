class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        result = [[0] * (len(word2) + 1) for _ in range(2)]
        for i1 in range(len(word1), -1, -1):
            for i2 in range(len(word2), -1, -1):
                if i1 >= len(word1):
                    result[i1%2][i2] = max(0, len(word2)-i2)
                    continue

                if i2 >= len(word2):
                    result[i1%2][i2] = max(0, len(word1)-i1)
                    continue

                if word1[i1] == word2[i2]:
                    result[i1%2][i2] = result[(i1+1)%2][i2+1]
                else:
                    result[i1%2][i2] = min(result[i1%2][i2+1]+1, result[(i1+1)%2][i2]+1, result[(i1+1)%2][i2+1]+1)

        return result[0%2][0]
