def letterCombinations(digits):
	a = range(10)
	b = ["*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz", " "]
	a.pop(0)
	a.append(0)
	d = dict(zip(a,b))
	result = []
	for x in digits:
		s = ""
		for y in xrange(0,len(d[int(x)])):
			s += d[int(x)][y]
			break
		result.append(s)
	print result

letterCombinations("123")