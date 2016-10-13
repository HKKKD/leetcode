def findMin(nums):
	array = sorted(nums)
	for i in xrange(0,len(nums)):
		nn = []
		nn = nums[i:] + nums[:i]
		if nn == array:
			return nums[i]
	return False

print findMin([4,5,6,7,0,1,2,3])