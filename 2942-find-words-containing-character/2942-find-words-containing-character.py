class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        for i,word in enumerate(words):
            for j in range(len(word)):
                if(words[i][j]==x):
                    res.append(i)
                    break
        return res


        