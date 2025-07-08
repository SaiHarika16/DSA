class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        previous_rows=self.generate(numRows-1)
        new_row=[1]*numRows
        for i in range(1,numRows-1):
            new_row[i]=previous_rows[-1][i]+previous_rows[-1][i-1]
        previous_rows.append(new_row)
        return previous_rows


        