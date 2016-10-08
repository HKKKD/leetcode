def maxSubArray(nums):
	dp = list()
	dp.append(nums[0])
	end = dp[0]
	for x in xrange(1,len(nums)):
		if dp[x-1] > 0:
			dp.append(nums[x] + dp[x-1])
		else:
			dp.append(nums[x])
		end = max(end,dp[x])
	print end
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])