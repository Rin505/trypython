pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetables": 11,
    "buffalo chicken": 12
}
pizzas["bacon"] = 14 # adding new
pizzas["cheese"] = 8  # changing the price for "cheese" pizza

if pizzas["vegetables"] < 12:   #manipulating if smth
    print("Pizzas with vegetables for sale!")

for pie in pizzas:
    print(pie)

for pie, price in pizzas.items():
    print(price)

for pie, price in pizzas.items():
   print("A whole {} pizza costs ${}".format(pie, price))

for pie, price in pizzas.items():
    print("A whole " + pie + " pizza costs $" + str(price))

print(pizzas)