class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def dfs(i, j, load):
            nonlocal robot, factory, m, n

            # base1; we processed all th robots
            if i >= m:
                return 0

            # base2; we checked all factories but some robots are not repaired
            if j >= n:
                return float('inf')

            # seen before
            if (i, j, load) in memo:
                return memo[(i, j, load)]

            # case1; skip processing ith robot at j th factory
            skip = dfs(i, j + 1, 0)

            # case2; use jth factory to repair ith robot
            take = float('inf')
            
            # make sure jth factory can process more load
            if factory[j][1] > load:
                distance = abs(robot[i] - factory[j][0])
                new_load = load + 1
                take = distance + dfs(i + 1, j, new_load)

            # update
            memo[(i, j, load)] = min(skip, take)

            return memo[(i, j, load)]

        m, n = len(robot), len(factory)

        # memo[(i, j, load)] := min distance of processing robot[i:] with factory[j:] while the jth factory has current total load being used 
        memo = dict()

        # 1. sort robot & factory increasingly 
        robot = sorted(robot)
        factory = sorted(factory)

        # 2. run dfs
        return dfs(0, 0, 0)
        