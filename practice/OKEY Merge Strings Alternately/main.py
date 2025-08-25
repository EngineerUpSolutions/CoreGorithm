class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        merge = []
        while i < len(word1) and j < len(word2):
            merge.append(word1[i])
            merge.append(word2[j])
            i +=1
            j +=1
        if i < len(word1):
            merge.append(word1[i:])
        elif j < len(word2):
            merge.append(word2[j:])
        return "".join(merge)

word1 = "abc"
word2 = "pqr"
s = Solution()
print(s.mergeAlternately(word1,word2))