class Solution:
    def maxUniqueSplit(self, s: str) -> int:
    
        result = 0 
        memo = set() # contains all subsets so far
        def backtrack(i,curr):
            nonlocal result
            if i == len(s):
                if curr and (curr not in memo):
                    result = max(len(memo)+1,result)
                return
                     
            curr += s[i]
            # count number of substrings if we include curr and start a new subset
            if curr not in memo:
                memo.add(curr)
                backtrack(i+1,"")
                memo.remove(curr)

            # count number of substrings if we keep adding to the curr substring
            backtrack(i+1,curr)

        backtrack(0,"")
        return result
        
        