class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])

        def dfs(r,c):
            if (r<0 or c<0 or r==rows or c==cols or not  grid[r][c] or (r,c) in visit):
                return 0
            visit.add((r,c))
            res=1
            direct=[[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in direct:
                res+= dfs(r+dr,c+dc)
            return res
        land,borderLand=0,0
        visit=set()
        for r in range(rows):
            for c in range(cols):
                land+=grid[r][c]
                if (grid[r][c] and (r,c) not in visit and (c in [0,cols-1] or r in[0,rows-1])):
                    borderLand+= dfs(r,c)
        return land-borderLand                        
        