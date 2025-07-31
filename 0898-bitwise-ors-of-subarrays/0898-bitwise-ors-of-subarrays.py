class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans=set()
        curr=set()
        for i in arr:
            curr={i} | {y|i for y in curr}
            ans.update(curr)
        return len(ans)
        