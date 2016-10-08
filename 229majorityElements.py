def majorityElements(nums):
	d = dict()
	for x in nums:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	for key, value in d.items():
		if value <= len(nums)/3:
			d.pop(key)
	return d.keys()
print majorityElements([1,1,1,3,3,3,4])
