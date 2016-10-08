def nthUglyNumber(n):
	def isUgly(num):
		if num==1:
			return True
		if num != 0:
			while num%2==0:
				num = num/2
			while num%3==0:
				num = num/3
			while num%5==0:
				num = num/5
		if num>=7 or num<=0:
			return False
		else:
			return True
	tar = 0
	flag = 0
	while flag!=n:
		if isUgly(tar):
			flag += 1
		tar += 1
	return tar-1

print nthUglyNumber(10)
