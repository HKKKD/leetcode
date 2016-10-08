def myAtoi(str):
	if len(str) <= 0:
		return 0
	ma = 2147483647
	mi = -2147483648
	num = 0
	sign = 1
	i = 0
	while str[i] == " " and i < len(str):
		i += 1
	if str[i] == "+":
		i += 1
	elif str[i] == "-":
		sign = -1
		i += 1	
	while i < len(str):
		if str[i] < "0" or str[i] > "9":
			break
		num = num*10 + ord(str[i]) - ord("0")
		i += 1
	if num * sign > ma:
		return ma
	elif num * sign < mi:
		return mi
	return num * sign

print myAtoi("2147483648")