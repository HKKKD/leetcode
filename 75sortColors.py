def sortColors(nums):
	l,r = 0,len(nums)-1
	x = 0
	while x < r+1:
		if nums[x] == 0:
			nums[x],nums[l] = nums[l],nums[x]
			x += 1
			l += 1
		elif nums[x] == 2:
			nums[x],nums[r] = nums[r],nums[x]
			r -= 1
			print 's'
		else:
			x += 1
	return nums

print sortColors([1,1,1,2,0])