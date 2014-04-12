prices = {
          'ACME':45.23,
          'AAPL':612.78,
          'IBM':205.55,
          'HPQ':37.20,
          'FB':10.75
          }

false_min_price = min(prices)
print(false_min_price)

min_price = min(zip(prices.values(), prices.keys())) #zip will create tuples
print(min_price)