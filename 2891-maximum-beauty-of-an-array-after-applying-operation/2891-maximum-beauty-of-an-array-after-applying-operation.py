class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()   
        start = 0   
        ans = 0  
        for end in range(len(nums)): 
             
            while nums[end] - nums[start] > 2 * k: 
                start += 1 
            ans = max(ans, end - start + 1) 
        return ans 
        