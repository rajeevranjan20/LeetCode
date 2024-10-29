from typing import List
from collections import deque

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns
        m, n = len(grid), len(grid[0])
        
        # Define possible movements in the row direction (up, no move, down)
        direction = [-1, 0, 1]
        
        # Initialize the maximum count of valid moves
        maxcount = 0
        
        # Set to keep track of visited states to avoid processing the same state multiple times
        seen = set()
        
        # Iterate over all rows to start BFS from the first column
        for idx in range(m):
            # Initialize the queue with the starting position and move count
            q = deque([[idx, 0, 0]])
            while q:
                i, j, count = q.popleft()
                
                # Continue if the current state has already been processed
                if (i, j, count) in seen:
                    continue
                
                # Add the current state to the seen set
                seen.add((i, j, count))
                
                # Update the maximum count of moves
                if count > maxcount:
                    maxcount = count
                
                # Explore all possible directions
                for ni in direction:
                    if 0 <= i + ni < m and 0 < j + 1 < n and grid[i + ni][j + 1] > grid[i][j] and count + 1 == j + 1 and (i + ni,  j + 1, count + 1) not in seen:
                        q.append([i + ni, j + 1, count + 1])
        
        # Return the maximum number of valid moves found
        return maxcount
        