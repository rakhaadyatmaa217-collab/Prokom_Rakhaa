my_pizzas = ["pepperoni", "cheese", "mushroom"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("vegetarian")
friend_pizzas.append("hawaiian")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
