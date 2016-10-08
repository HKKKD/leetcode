def addDigits(num):
	array = []
	for i in range(1,len(str(num))+1):
		array.append(num%10)
		num = (num - num%10)/10
	result = sum(array)
	if result>9:
		return addDigits(result)
	else:
		return sum(array)

print addDigits(19)