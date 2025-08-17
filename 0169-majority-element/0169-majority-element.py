class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''c=Counter(nums)
        n=len(nums)
        for num,freq in c.items():
            if freq>n/2:
                return num'''
        d={}
        n=len(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>n/2:
                return i      