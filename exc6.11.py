cities = {
    "surakarta": {
        "country": "Indonesia",
        "population": 522000,
        "fact": "Dikenal dengan budaya Jawa dan batik.",
    },
    "tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Merupakan ibu kota Jepang.",
    },
    "paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Terkenal dengan Menara Eiffel.",
    },
}
for city, info in cities.items():
    print(f"{city.title()}, {info['country']}")
    print(f"Population: {info['population']:,}")
    print(f"Fact: {info['fact']}\n")
