def maxProfit(prices):
	result = 0
	m = float('inf')
	for x in prices:
		if x <= m:
			m = x
		if x > m:
			result = max(result, x-m) 
	return result

print maxProfit([7,2,4,1])