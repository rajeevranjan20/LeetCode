class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closet=nums[0]
        for x in nums:
            if abs(x)<abs(closet):
                closet=x
        if closet<0 and abs(closet) in nums:
            return abs(closet)        
        else:
            return closet