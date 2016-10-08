def romanToInt(s):
	roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	result = 0
	for x in xrange(0,len(s)-1):
		if s[x] not in "IXC":
			print s[x]
			result += roman[s[x]]
		elif roman[s[x]] < roman[s[x+1]]:
			result -= roman[s[x]]
		else:
			result += roman[s[x]]
	result += roman[s[-1]]
	return result
		
print romanToInt("DCXXI")