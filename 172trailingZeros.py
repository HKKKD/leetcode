def trailingZeros(n):
		count = 0
		while n >= 1:
			count += n/5
			n /= 5
		return count

print trailingZeros(150)