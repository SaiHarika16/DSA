class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum={}
        curr_sum=0
        count=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                curr_sum+=mat[i][j]
            row_sum[i]=curr_sum
            curr_sum=0
        col_sum={}
        curr_sum=0
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                curr_sum+=mat[j][i]
            col_sum[i]=curr_sum
            curr_sum=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and row_sum[i]==1 and col_sum[j]==1:
                    count+=1
        return count