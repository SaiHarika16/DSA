class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i<j and nums[i]<nums[j]:
                    diff=nums[j]-nums[i]
                    max_diff=max(diff,max_diff)
        if max_diff!=0:
            return max_diff
        return -1
        
        