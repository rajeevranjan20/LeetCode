class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res=0
        cntOne=0
        for c in s:
            if c=="1":
                cntOne+=1
            else:
                res=min(res+1,cntOne)
        return res    
        