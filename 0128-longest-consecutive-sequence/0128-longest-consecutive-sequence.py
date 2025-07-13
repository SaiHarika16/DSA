class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        count=0
        curr_count=1
        for i in range(1,len(nums)):
            if(nums[i-1]==nums[i]):
                continue
            elif nums[i-1]+1==nums[i]:
                curr_count+=1
            else:
                count=max(count,curr_count)
                curr_count=1
        return max(count,curr_count)



        