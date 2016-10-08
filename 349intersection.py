def intersection(nums1, nums2):
	array = set()
	for x in nums1:
		if x in nums2:
			array.add(x)
	return list(array)

print intersection([1, 2, 2, 1,], [2, 2])