def containsDuplicate(nums):
	array = set(nums)
	if len(array) == len(nums):
		return False
	else:
		return True