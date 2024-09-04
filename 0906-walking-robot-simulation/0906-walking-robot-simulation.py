class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs=set(map(tuple,obstacles))

        direction_vectors={
            'N':(0,1),
            'E':(1,0),
            'S':(0,-1),
            'W':(-1,0)
        }

        dirChangeMap={
            "E":["N","S"],
            "N":["W","E"],
            "W":["S","N"],
            "S":["E","W"]
        }

        currDirection="N"
        currPos=[0,0]
        maxDist=0

        for d in commands:
            if d>0:
                dx,dy=direction_vectors[currDirection]
                for _ in range(d):
                    nextX,nextY=currPos[0]+dx,currPos[1]+dy
                    if (nextX,nextY) in obs:
                        break
                    currPos=[nextX,nextY]
                maxDist=max(maxDist,currPos[0]**2 + currPos[1]**2)        
            else:
                currDirection=dirChangeMap[currDirection][d]
        return maxDist        