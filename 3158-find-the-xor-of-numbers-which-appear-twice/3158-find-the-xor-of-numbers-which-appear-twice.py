class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in set(nums):
            if(nums.count(i)==2):
                res^=i
        return res

        