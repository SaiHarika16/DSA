class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        nums_s=[]
        for i in nums:
            while nums_s and nums_s[-1]==i:
                i+=nums_s.pop()
            nums_s.append(i)
        return nums_s