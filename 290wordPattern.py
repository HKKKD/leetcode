def wordPattern(pattern, str):
	str = str.split(' ')
	pattern = list(pattern)
	if len(str) != len(pattern):
		return False
	pd = dict(); sd = dict();
	for x in range(0,len(str)):
		if pattern[x] in pd:
			pd[pattern[x]].append(x)
		else:
			pd[pattern[x]] = [x]
		if str[x] in sd:
			sd[str[x]].append(x)
		else:
			sd[str[x]] = [x]
	print pd,'\n',sd
	return sorted(pd.values()) == sorted(sd.values())
	


print wordPattern("ab", "b c")