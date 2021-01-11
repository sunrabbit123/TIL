input1 = [7, 1, 5, 3, 6, 4]
output = 5

# 1. Brute force
def maxProfit(prices) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prieces)):
            max_price = max(prices[j] - price, max_price)

    return max_price

# 2. 저점과 현재 값과의 차이 계산
def maxProfit(prices) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit
    
