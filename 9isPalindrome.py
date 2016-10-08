def isPalindrome(x):
	old_x = x
	result = 0
	a = len(str(x)) - 1
	while a >= 0:
		result += x%10 * 10**a
		x = (x - x%10)/10
		a -= 1
	if result == old_x:
		return True
	else:
		return False

print isPalindrome(1221)