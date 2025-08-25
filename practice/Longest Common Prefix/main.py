class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            if not strs:
                return ""
            strs.sort(key=len)          # start from the shortest
            prefix = strs[0]
            for w in strs[1:]:
                while prefix and not w.startswith(prefix):
                    prefix = prefix[:-1]
                if not prefix:
                    return ""
            return prefix
s=Solution()
strs = ["flower","flow","flowes"]
print(s.longestCommonPrefix(strs))