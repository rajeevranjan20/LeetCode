class Solution:
	def zeroFilledSubarray(self, nums: List[int]) -> int:
		"""pattern  :1:1,2:3,3:6,4:10,5:15,6:21"""

		dp = [0 for i in range(max(100,len(nums)+1))]
		dp[1] = 1
		dp[2] = 3
		for i in range(3,len(nums)+1):
			dp[i] = dp[i-1]+i
		res = 0
		count = 0
		for i in nums:
			if i ==0:
				count +=1
			else:
				res+= dp[count]
				count = 0
		res+=dp[count]
		return res    

        