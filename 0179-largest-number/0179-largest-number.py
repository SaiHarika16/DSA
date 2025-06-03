#from functools import cmp_to_key 
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str=list(map(str,nums))
        nums_str.sort(key=lambda x:x*10,reverse=True)
        res="".join(nums_str)
        if res[0]=="0":
            return "0"
        return res
        