class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix1=list(zip(*matrix))
        res=[list(row[::-1]) for row in matrix1]
        for i in range(len(matrix)):
            matrix[i] = res[i]
        