class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max_sum=float("-inf")
        for i in range(0,len(nums)):
            sum+=nums[i]
            max_sum=max(sum,max_sum)
            if sum<0:
                sum=0
        return max_sum

        