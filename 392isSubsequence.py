def isSubsequence(s,t):
		j = 0
		for i in xrange(0,len(t)):
			if j == len(s):
				return True
			if t[i] == s[j]:
				j += 1
		return j == len(s)

print isSubsequence('axc','ahbgbc')