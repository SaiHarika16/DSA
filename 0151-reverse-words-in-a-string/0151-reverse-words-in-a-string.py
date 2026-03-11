class Solution:
    def reverseWords(self, s: str) -> str:
        curr=""
        s_list=[]
        for i in s:
            if i!=" ":
                curr+=i
            else:
                if curr:
                    s_list.append(curr)
                    curr=""
        if curr:
            s_list.append(curr)
        s_list=s_list[::-1]
        res=""
        for i in range(len(s_list)):
            res+=s_list[i]
            if i!=len(s_list)-1:
                res+=" "
        return res