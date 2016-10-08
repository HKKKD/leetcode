def compareVersion(version1, version2):
		v1 = list(); v2 = list()
		if '.' not in version1:
			v1.append(version1)
			v1.append('0')
		else:
			v1 = version1.split('.', 1)
		if '.' not in version2:
			v2.append(version2)
			v2.append('0')
		else:
			v2 = version2.split('.', 1)
		if int(v1[0]) > int(v2[0]):
			return 1
		elif int(v1[0]) < int(v2[0]):
			return -1
		else:
			if int(v1[1])> int(v2[1]):
				return 1
			elif int(v1[1]) < int(v2[1]):
				return -1
			else:
				return 0

print compareVersion("01","1")