def firstUniqChar(s):
	d = dict()
	for x in s:
		if x not in d:
			d[x] = s.index(x)
		else:
			d[x] += 1
	res = len(s)
	for k,v in d.iteritems():
		if v == s.index(k):
			res = min(res, s.index(k))
	if res < len(s):
		return res
	else:
		return -1

print firstUniqChar('loveleetcode')