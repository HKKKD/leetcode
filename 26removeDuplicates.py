def removeDuplicates(nums):
	l = 0; r = 1	
	while r < len(nums):
		if nums[r] == nums[l]:
			nums.pop(r)
		else:
			l += 1
			r = l+1
	return len(nums)

print removeDuplicates([1,1,2])