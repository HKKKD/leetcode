def isIsomorphic(s, t):
		s = list(s)
		t = list(t)
		if len(s) != len(t):
			return False
		pd = dict(); sd = dict();
		for x in range(0,len(s)):
			if t[x] in pd:
				pd[t[x]].append(x)
			else:
				pd[t[x]] = [x]
			if s[x] in sd:
				sd[s[x]].append(x)
			else:
				sd[s[x]] = [x]
		print pd.values(),'\n',sd.values()
		for bb in pd.values():
			if bb in sd.values():
				pass
			else:
				return False
		return True

print isIsomorphic("ab", "aa")