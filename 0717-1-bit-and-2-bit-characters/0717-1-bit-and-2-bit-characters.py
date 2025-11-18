class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        cl=[]
        while i<len(bits):
            if(bits[i]==0):
                i+=1
                cl.append(1)
            elif(bits[i:i+2]==[1,0] or bits[i:i+2]==[1,1]):
                i+=2
                cl.append(2)
            else:
                pass
        return (cl[-1]==1)    