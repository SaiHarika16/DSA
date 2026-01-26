class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        res_sum=float("-inf")
        for i in range(len(nums)):
            curr_sum+=nums[i] 
            res_sum=max(curr_sum,res_sum)
            if curr_sum<0:
                curr_sum=0
        return res_sum