class Solution(object):
    def sortArray(self, n):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(n)==1:
            return n
        if len(n)>1:
            mid=len(n)//2
            left_list=n[:mid]
            right_list=n[mid:]
            self.sortArray(left_list)
            self.sortArray(right_list)
            i=0
            j=0
            k=0
            while i<len(left_list) and j<len(right_list):
                if(left_list[i]<right_list[j]):
                    n[k]=left_list[i]
                    i+=1
                else:
                    n[k]=right_list[j]
                    j+=1
                k+=1
            while i<len(left_list):
                    n[k]=left_list[i]
                    i+=1
                    k+=1
            while j<len(right_list):
                n[k]=right_list[j]
                j+=1
                k+=1
            return n
        