def max_profit(prices):
    # max_price = 1
    # min_price = 0
    # profit = 0
    
    # for i in range(1, len(prices)-1): 
    #     if prices[i] < prices[min_price] :
    #         min_price = i
        
    # if min_price == len(prices) - 2:
    #     max_price = len(prices) - 1
    #     profit = prices[max_price] - prices[min_price]
    #     if profit >= 0:
    #         return profit
    #     else:
    #         return 0

    # max_price = min_price 

    # for j in range(min_price, len(prices)):
    #     if prices[j] > prices[max_price]:
    #         max_price = j
    
    # profit = prices[max_price] - prices[min_price]
    # if profit >= 0:
    #     return profit
    # else:
    #     return 0
        
    # maximum_profit = prices[max_price] - prices[min_price]
    # return maximum_profit
    
# second way
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""