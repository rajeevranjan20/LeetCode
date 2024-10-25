class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result=[]
        for dir in folder:
            if not result or not dir.startswith(result[-1]+'/'):
                result.append(dir)
        return result    
        