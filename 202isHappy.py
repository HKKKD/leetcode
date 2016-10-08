def isHappy(n):
	array = []
	result = 0
	for i in range(1,len(str(n))+1):
		array.append(n%10)
		n = (n - n%10)/10
	for x in array:
		result += x**2
	try:
			if result==1:
				return True
			else:
				return isHappy(result)
	except RuntimeError:
		return False

print isHappy(54)