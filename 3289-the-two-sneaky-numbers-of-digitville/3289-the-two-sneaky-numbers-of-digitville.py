class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if nums.count(i)==2:
                res.append(i)
        return list(set(res))  