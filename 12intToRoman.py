def inToRoman(num):
	key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	value = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	array = []
	i = 0
	while num > 0:
		count = num / key[i]
		num %= key[i]
		while count > 0:
			array.append(value[i])
			count -= 1
		i += 1
	return ''.join(array)

print inToRoman(12)