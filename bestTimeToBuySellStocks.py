def maxProfit(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i != j and j > i:
                if best < prices[j] - prices[i]:
                    best = prices[j] - prices[i]
    return best

print(maxProfit([7,6,4,3,1]))