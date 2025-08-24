class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        for i in range(len(s)):
            #if the next exits
            if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
                total -= val[s[i]]
        
            else:
                total += val[s[i]]
            

            # print(val[s[i]])
        return total
Roman = "IXX"
s = Solution()
print(s.romanToInt(Roman))