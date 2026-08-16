class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string=str()
        total=max(len(word1),len(word2))
        for i in range(0,total):
            if i<len(word1):
                string+=word1[i]
            if i<len(word2):
                string+=word2[i]    


        return string   
