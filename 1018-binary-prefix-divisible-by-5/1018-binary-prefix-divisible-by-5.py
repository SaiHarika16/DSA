class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr=0
        res=[]
        for i in range(len(nums)):
            curr=(curr*2+nums[i])%5
            res.append(curr==0)
        return res