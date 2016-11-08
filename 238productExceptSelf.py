def productExceptSelf(nums):
	cur = 1
	res = []
	l = len(nums)
	for i in xrange(0,l):
		res.append(cur)
		cur *= nums[i]
	cur = 1
	for i in xrange(l-1,-1,-1):
		res[i] *= cur
		cur *= nums[i]
	return res

print productExceptSelf([1,2,3,4])