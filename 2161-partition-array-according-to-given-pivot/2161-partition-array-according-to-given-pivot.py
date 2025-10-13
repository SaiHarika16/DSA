class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_l=[]
        right_l=[]
        equal_l=[]
        for i in nums:
            if i<pivot:
                less_l.append(i)
            elif(i>pivot):
                right_l.append(i)
            else:
                equal_l.append(i)
        return less_l+equal_l+right_l