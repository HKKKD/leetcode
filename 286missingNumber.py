def missingNumber(nums):
	if 0 not in nums:
		return 0
	s = (0+len(nums))*(len(nums)+1)/2
	ss = sum(nums)
	if s == ss:
		return len(nums)
	else:
		return s-ss

print missingNumber([1])