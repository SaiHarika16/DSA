class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=Counter(nums)
        for num,freq in counts.items():
            if freq>1:
                return num
        
        