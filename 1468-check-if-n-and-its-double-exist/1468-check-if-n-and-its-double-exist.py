class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return (a:=Counter(arr))[0]>=2 or sum([1 if 2*i in a and i!=0 else 0 for i in arr])>0
        