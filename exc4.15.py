# Contoh code review: tiga program sederhana ditulis ulang dengan gaya PEP 8.
def show_pizzas(pizzas):
    for pizza in pizzas:
        print(pizza.title())


def show_animals(animals):
    for animal in animals:
        print(f"A {animal} would make a great pet.")


def show_cubes(numbers):
    for number in numbers:
        print(number ** 3)


show_pizzas(["pepperoni", "cheese", "mushroom"])
show_animals(["dog", "cat", "rabbit"])
show_cubes(range(1, 4))
