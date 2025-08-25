class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for letter in t:
            if i < len(s) and letter == s[i]:
                i +=1
        return i == len(s)




# def isSubsequence(s: str, t: str) -> bool:
#     i = j = 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#     return i == len(s)




s = "abc"
t = "ahbgdc"
solution = Solution()
print(solution.mergeAlternately(s,t))
