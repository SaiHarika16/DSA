class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=nums[0]
        res_sum=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],nums[i]+curr_sum)
            res_sum=max(curr_sum,res_sum)
        return res_sum
        