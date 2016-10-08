def countPrimes(n):
		isPrime = [True]*n
		i = 2
		while i*i < n:
			if isPrime[i] is not True:
				pass
			j = i*i
			while j < n:
				isPrime[j] = False
				j += i
			i += 1
		count = 0
		k = 2
		while k<n:
			if isPrime[k]:
				count += 1
			k += 1
		return count

print countPrimes(499979)
