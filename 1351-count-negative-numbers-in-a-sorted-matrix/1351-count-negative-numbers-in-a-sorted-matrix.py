class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        n=len(grid)
        row=0
        col=cols-1
        while row<rows and col>=0:
            if grid[row][col]<0:
                count+=rows-row
                col-=1
            else:
                row+=1
        return count