def lengthOfLastWord(s):
	array = s.split()
	if len(array) == 0:
		return 0
	else:
		return len(array[-1])

print lengthOfLastWord('')