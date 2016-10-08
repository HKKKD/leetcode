import collections
def intersect(nums1,nums2):
	cnt = collections.Counter()
	for val in nums1:
		cnt[val] += 1
	ans = []
	for val in nums2:
		if cnt.has_key(val) and cnt[val] > 0:
			ans.append(val)
			cnt[val] -= 1
	return ans

print intersect([1,2,3,2,1,1], [2,3,2,2,1,1])
