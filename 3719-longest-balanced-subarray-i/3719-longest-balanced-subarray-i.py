class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ec=0
        oc=0
        res=0
        curr_nums=[]
        for i in range(len(nums)):
            es=set()
            os=set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    es.add(nums[j])
                else:
                    os.add(nums[j])
                if len(es)==len(os):
                    res=max(res,j-i+1)
        return res