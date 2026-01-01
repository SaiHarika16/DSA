class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        res=[]
        for i in digits:
            i=str(i)
            s+=i
        s=str(int(s)+1)
        for i in s:
            res.append(int(i))
        return res
        