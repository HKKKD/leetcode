def readBinaryWatch(num):
	bin = [0,1]
	hour =  [ [a1,a2,a3,a4] for a1 in bin for a2 in bin for a3 in bin for a4 in bin ]
	minute =  [ [a1,a2,a3,a4,a5,a6] for a1 in bin for a2 in bin for a3 in bin for a4 in bin for a5 in bin for a6 in bin ]
	hour.remove([1,1,1,1])
	hour.remove([1,1,1,0])
	hour.remove([1,1,0,1])
	hour.remove([1,1,0,0])
	minute.remove([1,1,1,1,1,1])
	minute.remove([1,1,1,1,1,0])
	minute.remove([1,1,1,1,0,1])
	minute.remove([1,1,1,1,0,0])

	i = 0
	j = num-i
	result = []
	while j >= 0:
		for x in hour:
			if sum(x) == i:
				for y in minute:
					if sum(y) == j:
						result.append(x+y)

		i += 1
		j -= 1

	out = list()
	for t in result:
		t = ''.join(str(e) for e in t)
		out.append(str(int(t[:4], 2)) + ":" +str(int(t[4:], 2)).zfill(2)) 
	return out
print readBinaryWatch(8)