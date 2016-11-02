def titleToNumber(s):
	if not hasattr(titleToNumber, "counter"):
		titleToNumber.counter = 0
	a = list(chr(a+65) for a in range(26))
	b = list(range(27))[1::]
	arr = dict(zip(a,b))
	temp = s[-1:]
	s = s[:-1]
	result = 0
	result += arr[temp] * pow(26,titleToNumber.counter)
	titleToNumber.counter += 1
	if len(s) == 0:
		return result
	else:
		return titleToNumber(s) + result
	return 0

print titleToNumber('BA')