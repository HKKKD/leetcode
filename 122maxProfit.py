def maxProfit(prices):
	result = [prices[i] - prices[i-1] for i in range(1, len(prices))]
	return sum(a for a in result if a > 0)

print maxProfit([7,2,4,1])