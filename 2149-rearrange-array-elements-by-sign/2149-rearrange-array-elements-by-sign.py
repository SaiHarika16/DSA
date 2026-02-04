class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg_nums=[]
        pos_nums=[]
        res_nums=[]
        for i in nums:
            if i<0:
                neg_nums.append(i)
            else:
                pos_nums.append(i)
        for i in range(len(neg_nums)):
            res_nums.append(pos_nums[i])
            res_nums.append(neg_nums[i])
        return res_nums