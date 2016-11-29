def fizzBuzz(n):
	arr = []
	for i in xrange(1, n+1):
		if i % 3 == 0 and i % 5 != 0:
			arr.append('Fizz')
		elif i % 5 == 0 and i % 3 != 0:
			arr.append('Buzz')
		elif i % 15 == 0:
			arr.append('FizzBuzz')
		else:
			arr.append(str(i))
	return arr

print fizzBuzz(17)