def firstMissingPositive(nums):
		flag = 0
		if len(nums) <= 0:
			return 1
		elif len(nums) == 1 and (nums[0] == 1 or nums[0] == 0):
			return nums[0]+1
		elif len(nums) == 1 and nums[0] > 1:
			return nums[0]-1
		m = nums[0]
		for x in nums:
			if x < m:
				m = x
		mm = m
		for y in nums:
			if y-m == 2:
				if m > 0:
					return m+1
				else:
					m = y
				flag += 1
			elif y-m == 1:
				m = y
				flag += 1
			else:
				nums.remove(y)
				nums.append(y)
		if mm > 1:
			return mm-1
		if m > 1 and flag == 0:
			return m-1
		elif m+1 <= 0:
			return 1
		else:
			return m+1

print firstMissingPositive([2,3,1])
