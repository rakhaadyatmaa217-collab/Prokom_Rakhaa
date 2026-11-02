# Versi loop dari contoh foods.py dan animals.py.
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My foods:")
for food in my_foods:
    print(food)
print("My friend's foods:")
for food in friend_foods:
    print(food)
