def lexicalOrder(n):
	cur = 1
	res = []
	for x in range(n):
		res.append(cur)
		if cur * 10 <= n:
			cur  *= 10
		else:
			cur += 1
			while cur % 10 == 0:
				cur /= 10
			if cur > n:
				cur = cur/10 + 1
	return res

print lexicalOrder(20)