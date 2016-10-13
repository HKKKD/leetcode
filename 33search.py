def search(nums, target):
	for idx,val in enumerate(nums):
		if val == target:
			return idx
	return -1
print search([4,5,6,7,0,1,2],5)