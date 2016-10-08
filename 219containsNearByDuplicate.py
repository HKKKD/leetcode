def containsNearByDuplicate(nums, k):
	if len(nums) <= 1:
		return False
	d = dict()
	for x in xrange(0, len(nums)):
		if nums[x] in d:
			d[nums[x]].append(x)
		else:
			d[nums[x]] = [x]
	print d
	for value in d.values():
		if len(value) < 2:
			pass
		elif sorted([value[i+1]-value[i] for i in range(len(value)-1)])[0] <= k:
			return True
	return False
print containsNearByDuplicate([1,2], 2)