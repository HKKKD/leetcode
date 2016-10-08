def hammingWeight(n):
	return sum(int(x) for x in bin(n)[2::].zfill(32))

print hammingWeight(11)