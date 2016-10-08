def minSubArrayLen(s, nums):
		length = len(nums)
		d = dict()
		for x in range(0,length):
			midRe = nums[x]
			for y in range(x+1,length):
				if midRe >= s:
					return 1
				else:
					midRe += nums[y]
				if midRe >= s:
					d[x] = y-x+1
					break
		if len(d) >= 1:
			return d[min(d, key=d.get)]
		else:
			return 0

print minSubArrayLen(12,[1,1,1,1,1,1,10])