class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        allString=s1.split(' ')
        allString+=(s2.split(' '))
        counter=Counter(allString)
        ans=[]
        for s,cnt in counter.items():
            if cnt==1:
                ans.append(s)
        return ans
        