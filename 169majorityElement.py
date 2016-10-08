def majorityElement(nums):
	return sorted(nums)[int(len(nums)/2)]

print majorityElement([1,1,2,2,3,3,3,3])