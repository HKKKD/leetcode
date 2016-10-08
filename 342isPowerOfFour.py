def isPowerOfFour(n):
		x = 1
		if n <= 0:
			return False
		elif n == 1:
			return True
		while True:
			x = x << 2
			print x
			if x == n:
				return True
			elif x > n:
				return False

print isPowerOfFour(19)