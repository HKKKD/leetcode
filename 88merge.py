def merge(nums1, m, nums2, n):
	i, j, k = m-1, n-1, m+n-1
	while i >= 0 and j >= 0:
		if nums1[i] > nums2[j]:
			nums1[k] = nums1[i]
			k -= 1
			i -= 1
		else:
			nums1[k] = nums2[j]
			k -= 1
			j -= 1
	while i >= 0:
		nums1[k] = nums1[i]
		k -= 1
		i -= 1
	while j >= 0:
		nums1[k] = nums2[j]
		k -= 1
		j -= 1
	return nums1

print merge([1,2],2,[3,4],2)