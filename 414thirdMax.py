def thirdMax(nums):
	a, b, c = float('-inf'), float('-inf'), float('-inf')
	for n in nums:
		if n in (a, b, c):
			continue
		if n > a:
			a, b, c = n, a, b
		if a > n > b:
			a, b, c = a, n, b
		if b > n > c:
			a, b, c = a, b, n
	return c if c != float('-inf') else a

print thirdMax([2,3,3,1,3,1,3])