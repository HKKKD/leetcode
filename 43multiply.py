def multiply(num1, num2):
	if len(num1) < len(num2):
		num1, num2 = num2, num1
	result = 0
	for x in xrange(0,len(num1)):
		result += int(num1[x:x+1]) * int(num2) * 10**(len(num1)-(x+1))
	return str(result)

print multiply("11", "13")
