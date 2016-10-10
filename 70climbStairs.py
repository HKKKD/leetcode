import math
def climbStairs(n):
	if n % 2 == 0:
		low = n/2
		high = n	
		sums = 0
		l = list(2*x for x in xrange(low+1))
		print l,low
		for x in xrange(low,high+1):
			print sums,x,l[x-low]
			sums += math.factorial(x) / ( math.factorial(l[x-low]) * math.factorial(x - l[x-low]) )
	else:
		low = n/2+1
		high = n
		sums = 0
		l = list(2*x+1 for x in xrange(low))
		print l,low
		for x in xrange(low,high+1):
			print sums,x,l[x-low]
			sums += math.factorial(x) / ( math.factorial(l[x-low]) * math.factorial(x - l[x-low]) )		
	return sums

print climbStairs(3)