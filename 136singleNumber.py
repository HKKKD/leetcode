def singleNumber(nums):
	s = set(nums)
	d = dict()
	for x in nums:
		if x in s:
			if x in d:
				d[x] += 1
			else:
				d[x] = 1
	for key,value in d.iteritems():
		if value == 1:
			return key


print singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])
