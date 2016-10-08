def findDuplicate(nums):
	nums.sort()
	l = 0; r = 1	
	while r < len(nums):
		if nums[r] == nums[l]:
			return nums[r]
		else:
			l += 1
			r = l+1

print findDuplicate([1,1])