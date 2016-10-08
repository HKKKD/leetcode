def lengthOfLongestSubstring(s):
	if len(s) <= 0:
		return 0
	l = 0
	r = l+1
	length = 1
	array = []
	array.append(s[0])
	while r < len(s):
		if s[r] not in array:
			array.append(s[r])
			r += 1
			if len(array) > length:
				length = len(array)
		else:
			if len(array) > length:
				length = len(array)
			l += 1
			r = l+1
			array = []
			array.append(s[l])
	print array
	return length

print lengthOfLongestSubstring("abcabcbb")
