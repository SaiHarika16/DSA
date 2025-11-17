class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idxs=[]
        for i in range(len(nums)):
            if(nums[i]==1):
                idxs.append(i)
        for i in range(len(idxs)-1):
            if(idxs[i+1]-idxs[i]<=2):
                return False
        return True