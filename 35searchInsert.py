def searchInsert(nums, target):
	if target <= nums[0]:
		return 0
	elif target > nums[-1]:
		return len(nums)
	for idx, val in enumerate(nums):
		if val == target:
			return idx
		elif val < target and idx+1 < len(nums) and nums[idx+1] > target:
			return idx+1

print searchInsert([2,5], 9)