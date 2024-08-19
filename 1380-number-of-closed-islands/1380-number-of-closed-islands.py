class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        len1,len2=len(grid),len(grid[0])
        ways=[(1,0),(0,1),(-1,0),(0,-1)]
        check1,check2=[0,len1-1],[0,len2-1]
        que=deque()
        count=0
        for i in range(len1):
            temp=check2 if i not in check1 else range(len2)
            for j in temp:
                if not grid[i][j]:
                    grid[i][j]=2
                    que.append((i,j))
                    while que:
                        x,y=que.popleft()
                        for dx,dy in ways:
                            new_x=x+dx
                            new_y=y+dy
                            if 0<=new_x<len1 and 0<=new_y<len2 and grid[new_x][new_y]==0:
                                grid[new_x][new_y]=2
                                que.append((new_x,new_y))
        for i in range(1,len1-1):
            for j in range(1,len2-1):
                if not grid[i][j]:
                    grid[i][j]=3
                    que.append((i,j))
                    while que:
                        x,y=que.popleft()
                        for dx,dy in ways:
                            new_x=x+dx
                            new_y=y+dy
                            if grid[new_x][new_y]==0:
                                grid[new_x][new_y]=3
                                que.append((new_x,new_y))
                    count+=1
        return count

          

        