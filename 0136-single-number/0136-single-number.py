class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''res=0
        for num in nums:
            res^=num
        return res'''
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        for num,freq in d.items():
            if freq==1:
                return num

        