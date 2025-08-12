class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_freq=0
        res=0
        for i in range(len(nums)):
            max_freq=max(max_freq,nums.count(nums[i]))
        for i in set(nums):
            if(nums.count(i)==max_freq):
                res+=max_freq
        return res
        
        