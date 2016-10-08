def countAndSay(n):
	a = "1"; count = 1
	if n == 1:
		return a
	while count != n:
		d = dict()
		t = list()
		s = ""
		for x in a:
			if x in d:
				d[x] += 1
			else:
				d[x] = 1
				t.append(x)
				s += "%d%s"%(d[x], x)
		print s,t,d,a
		a = str()
		for key in t:	
			a += "%d%s"%(d[key], key)
		count += 1

	return a

print countAndSay(5)

