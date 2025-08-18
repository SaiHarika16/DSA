class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freqs={}
        numbers=len(grid)**2
        for i in grid:
            for j in i:
                freqs[j]=freqs.get(j,0)+1
        #repeating=0
        #missing=0
        for num in range(1,numbers+1):
            if num not in freqs:
                missing=num
            elif freqs[num]==2:
                repeating=num
        return [repeating,missing]

        