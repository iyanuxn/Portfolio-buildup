class Solution:
    def romanToInt(self, s: str) -> int:
        val=0
        romanMap = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
        
        for i in range(len(s)):
            if i !=len(s)-1 and romanMap[s[i]] < romanMap[s[i+1]]:
                val = val - romanMap[s[i]] 
            else:
                val = val + romanMap[s[i]]
        
        return val