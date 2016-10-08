def strStr(haystack,needle):
	if len(needle):
		if needle in haystack:
			length = len(haystack) - len(needle) + 1
			for i in range(length):
				j = i
				k = 0
				while j < len(haystack) and k < len(needle) and haystack[j] == needle[k]:
					j += 1
					k += 1
				if k == len(needle):
					return i
		else:
			return -1
	else:
		return 0
print strStr("mississippi","issip")