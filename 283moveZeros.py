def moveZeros(nums):
	for x in nums:
		if x == 0:
			nums.remove(x)
			nums.append(x)
	print nums

moveZeros([0,1,0,3,12])