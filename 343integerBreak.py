def integerBreak(n):
	if n == 3 or n == 2:
		return n-1
	elif n == 4:
		return 4

	result = 1

	while n > 4:
		result *= 3
		n -= 3
	result *=n

	return result

print integerBreak(10)