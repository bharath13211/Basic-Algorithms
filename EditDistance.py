class EditDistance:
    def editDistance(self, word1, word2):
        m= len(word1)
        n = len(word2)
        out = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    out[i][j] = j
                elif j==0:
                    out[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    out[i][j] = out[i-1][j-1]
                else:
                    out[i][j] = 1+min(out[i-1][j],out[i][j-1],out[i-1][j-1])
        return out[m][n]
        