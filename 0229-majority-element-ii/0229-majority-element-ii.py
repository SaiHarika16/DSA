'''class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>len(nums)//3:
                    res.append(i)
        return res'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        threshold = len(nums) // 3

        for num in nums:
            d[num] = d.get(num, 0) + 1

        for key in d:
            if d[key] > threshold:
                result.append(key)

        return result

        