class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=defaultdict(list)
        sz=len(edges)
        for i in range(sz):
            u,v,cost=edges[i][0],edges[i][1],succProb[i]
            adj[u].append((cost,v))
            adj[v].append((cost,u))
        maxHeap=[(-1.0,start_node)]
        Prob=[0.0]*n 
        Prob[start_node]=1.0
        while maxHeap:
            cost,node=heapq.heappop(maxHeap)
            cost=-cost
            if node==end_node:return cost
            for ccost,cnode in adj[node]:
                newcost=ccost*cost
                if newcost>Prob[cnode]:
                    Prob[cnode]=newcost
                    heapq.heappush(maxHeap,(-newcost,cnode))  
        return 0.0

        