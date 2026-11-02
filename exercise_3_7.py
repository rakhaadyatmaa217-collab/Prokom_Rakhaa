# Exercise 3-7: Shrinking Guest List
guests = [
    "R.A. Kartini",
    "B.J. Habibie",
    "Albert Einstein",
    "Soekarno",
    "Nelson Mandela",
    "Mohammad Hatta"
]

print("Maaf, meja makan baru tidak akan tiba tepat waktu.")
print("Saya hanya bisa mengundang dua orang.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda.")

print("\nDua tamu yang tetap diundang:")
for guest in guests:
    print(f"{guest}, Anda tetap diundang makan malam.")

del guests[0]
del guests[0]

print("\nDaftar tamu setelah dihapus:")
print(guests)
