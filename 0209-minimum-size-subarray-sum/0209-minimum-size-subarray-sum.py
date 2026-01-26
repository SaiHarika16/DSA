class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum=0
        res=float("inf")
        left=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            while curr_sum>=target:
                curr_sum-=nums[left]
                res=min(res,i-left+1)
                left+=1
        return 0 if res==float("inf") else res