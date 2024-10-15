class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        blackCount=0
        for ch in s:
            if ch=='0':
                ans+=blackCount
            else:
                blackCount+=1
        return ans
        