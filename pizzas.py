pizzas = {
    "chess": 9,
    "pepperoni": 10,
    "vegetables": 11,
    "buffalo chicken": 12
}
def pizza():
 for pie, price in pizzas.items():
   print("A whole {} pizza costs ${}".format(pie, price))

pizza()