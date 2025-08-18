class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res=[]
        for i in grid:
            for j in i:
                res.append(j)
        n=len(grid)
        missingnumber=0
        repeatingnumber=0
        for i in range(1,n**2+1):
            if i not in res:
                missingnumber=i
        for j in range(1,n**2+1):
            if(res.count(j)==2):
                repeatingnumber=j
        return [repeatingnumber,missingnumber]

        