def addStrings(num1, num2):
	num1 = list(int(num1[x]) for x in xrange(len(num1)-1,-1,-1))
	num2 = list(int(num2[x]) for x in xrange(len(num2)-1,-1,-1))
	l1,l2 = len(num1),len(num2)
	if l1 < l2:
		num1, num2 = num2, num1
		l1, l2 = l2, l1
	i,j = 0,0
	while j < l2:
		num1[i] += num2[j]
		if num1[i] > 9:
			num1[i] %= 10
			if i == l1-1:
				num1.append(1)
			else:
				num1[i+1] += 1
		i += 1
		j += 1	
	for x in xrange(0,l1-1):
		if num1[x] >= 10:
			num1[x] %= 10
			if x == l1-1:
				num1.append(1)
			else:
				num1[x+1] += 1
	result = ''.join(str(num1[x]) for x in xrange(len(num1)-1,-1,-1))	
	return result

print addStrings("71","168899993")