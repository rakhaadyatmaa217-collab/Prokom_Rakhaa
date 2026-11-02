# Contoh tiga function dengan gaya PEP 8.
def describe_pet(animal, name):
    print(f"I have a {animal} named {name.title()}.")


def make_shirt(size, message):
    print(f"Size: {size}; message: {message}")


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


describe_pet("hamster", "harry")
make_shirt("M", "Python")
print(city_country("surakarta", "indonesia"))
