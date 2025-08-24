class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        r = []
        while i < len(word1) and j < len(word2):
            r.append(word1[i])
            r.append(word2[j])
            i +=1
            j +=1
        if i < len(word1):
            r.append(word1[i:])
        elif j < len(word2):
            r.append(word2[j:])
        return "".join(r)

word1 = "abc"
word2 = "pqrlist"
solution = Solution()
print(solution.mergeAlternately(word1,word2))



# two‑pointer pattern 

# Time Complexity: O(n + m)
# Space Complexity: O(n + m) (for the result string)