class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        res = []
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        for query in queries:
            if self.checkQuery(graph, query):
                res.append(True)
            else:
                res.append(False)
        return res

    def checkQuery(self, graph, query):
        startNode, endNode = query[0], query[1]
        visited = set()
        q = deque([startNode])
        while q:
            node = q.popleft()
            visited.add(node)

            if node == endNode:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
        
        return False