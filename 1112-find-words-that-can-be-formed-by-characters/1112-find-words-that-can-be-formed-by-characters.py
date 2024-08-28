class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=Counter(chars)
        res=0
        for w in words:
            curr_word=defaultdict(int)
            good=True
            for c in w:
                curr_word[c]+=1
                if c not in count or curr_word[c]>count[c]:
                    good=False
                    break
            if good:
                res+=len(w)
        return res                
        