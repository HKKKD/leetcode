def isValid(s):
		d = dict()
		for x in xrange(0,len(s)):
			if s[x] in d:
				d[s[x]].append(x)
			else:
				d[s[x]] = [x]

		if len(d)%2 != 0:
			return False
		elif len(d)/2 == 1:
			if ('(' and ')' in d and d['('] < d[')']) or ('{' and '}' in d and d['{'] < d['}']) or ('[' and ']' in d and d['['] < d[']']):
				return True
			else:
				return False
		elif len(d)/2 == 2:
			if ('(' and ')' not in d and d['['] < d[']'] and d['{'] < d['}']) or ('[' and ']' not in d and d['{'] < d['}'] and d['('] < d[')']) or ('{' and '}' not in d and d['('] < d[')'] and d['['] < d[']']):
				return True
			else:
				return False
		elif len(d)/2 == 3:
			if d['('] < d[')'] and d['{'] < d['}'] and d['['] < d[']']:
				return True
			else:
				return False
		else:
			return False

print isValid("([)]")