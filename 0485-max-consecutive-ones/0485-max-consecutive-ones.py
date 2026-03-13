class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        res=0
        for right in range(len(nums)):
            if nums[right]==0:
                res=max(res,right-left)
                left=right+1
        res=max(res,len(nums)-left)
        return res