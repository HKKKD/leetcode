def lengthOfLongestSubstring(s):
	last = list(-1 for _ in range(256))
	result = 0
	start = 0
	for index, value in enumerate(s):
		if last[ord(value)] == -1:
			result = max(result, (index) - start + 1)
		else:
			result = max(result, (index-1) - start + 1)
			for i in xrange(start,last[ord(value)]):
				last[ord(s[i])] = -1
			start = last[ord(value)] + 1
		last[ord(value)] = index
	return result
print lengthOfLongestSubstring("abcabcbb")
