class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        prevC = n
        newMat = [[0] * c for _ in range(r)] 
        
        for i in range(r * c):
            newMat[i // c][i % c] = mat[i // prevC][i % prevC]
        
        return newMat