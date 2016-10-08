def isPowerOfThree(n):
		if n == 1:
			return True
		if n <= 0 or n%3 != 0:
			return False
		while n%3 == 0:
			n = n/3
		if n == 1:
			return True
		else:
			return False
print isPowerOfThree(3)