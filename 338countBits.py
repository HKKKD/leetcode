def countBits(n):
	array = []
	for x in xrange(0,n+1):
		array.append(sum(int(t) for t in bin(x)[2::].zfill(32)))
	return array

print countBits(5)