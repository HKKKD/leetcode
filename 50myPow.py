def myPow(x,n):
	if n == 0:
		return 1
	v = pow(x, n/2)
	if n%2 == 0:
		return v*v
	else:
		return v*v*x
print myPow(2, 9)