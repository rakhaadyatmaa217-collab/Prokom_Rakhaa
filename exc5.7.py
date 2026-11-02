favorite_fruits = ["mango", "banana", "apple"]
fruit = input("Masukkan nama buah: ").lower()
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
else:
    print(f"{fruit.title()} is not in the favorite list.")
