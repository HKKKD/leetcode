def findMedianSortedArrays(nums1, nums2):
	def mergeSortedArrays(nums1, nums2):
		i, j, k = len(nums1)-1, len(nums2)-1, len(nums1)+len(nums2)-1
		array = [None] * (k+1)
		while i >= 0 and j >= 0:
			if nums1[i] > nums2[j]:
				array[k] = nums1[i]
				k -= 1
				i -= 1
			else:
				array[k] = nums2[j]
				k -= 1
				j -= 1
		while i >= 0:
			array[k] = nums1[i]
			k -= 1
			i -= 1
		while j >= 0:
			array[k] = nums2[j]
			k -= 1
			j -= 1
		return array
	result = mergeSortedArrays(nums1, nums2)
	if len(result) % 2 == 0:
		print "flag"
		print result[len(result)/2]-1,result[len(result)/2]
		return (result[len(result)/2-1] + result[len(result)/2]) / 2.0
	else:
		return result[(len(result)-1)/2]
print findMedianSortedArrays([1,2], [3,4])

