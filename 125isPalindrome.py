def isPalindrome(s):
	s = s.lower()
	l = 0
	r = len(s) - 1
	while l < r:
		if s[l].isalnum() is not True:
			l += 1
		elif s[r].isalnum() is not True:
			r -= 1
		elif s[l] != s[r]:
			return False
		else:
			l += 1
			r -= 1
	return True

print isPalindrome("ab")