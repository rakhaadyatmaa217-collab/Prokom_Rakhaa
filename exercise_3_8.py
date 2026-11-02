# Exercise 3-8: Seeing the World
places = ["Tokyo", "Iceland", "Seoul", "New York", "Swiss"]

print("Daftar awal:")
print(places)

print("\nUrutan alfabetis (sorted):")
print(sorted(places))

print("\nDaftar asli tidak berubah:")
print(places)

print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

print("\nDaftar asli tetap tidak berubah:")
print(places)

places.reverse()
print("\nSetelah reverse pertama:")
print(places)

places.reverse()
print("\nSetelah reverse kedua (kembali seperti awal):")
print(places)

places.sort()
print("\nSetelah sort alfabetis:")
print(places)

places.sort(reverse=True)
print("\nSetelah sort alfabetis terbalik:")
print(places)
