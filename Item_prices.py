items_prices = {"milk": 2.20, "bread": 10.11, "eggs": 22.15, "juice": 1.22,}

chosen_item = (input("Choose item: "))

if chosen_item in items_prices.keys():
    price = items_prices[chosen_item]
    print(chosen_item, "price is %s" % (price))

else:
    print("Item is not available.")
