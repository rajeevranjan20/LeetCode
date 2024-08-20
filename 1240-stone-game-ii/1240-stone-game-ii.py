class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp=[[0]*(n+1) for _ in range(n+1)]
        suffixSum=[0]*(n+1)

        for i in range(n-1,-1,-1):
            suffixSum[i]=suffixSum[i+1]+piles[i]
        for i in range(n-1,-1,-1):
            for m in range(1,n+1):
                for x in range(1,min(2*m,n-i)+1):
                    dp[i][m]=max(dp[i][m],suffixSum[i]-dp[i+x][max(m,x)])   
        return dp[0][1]             
        