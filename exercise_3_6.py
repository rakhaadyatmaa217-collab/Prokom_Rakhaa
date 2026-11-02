# Exercise 3-6: More Guests
guests = ["B.J. Habibie", "Soekarno", "Nelson Mandela"]

print("Saya menemukan meja makan yang lebih besar!")

guests.insert(0, "R.A. Kartini")
guests.insert(2, "Albert Einstein")
guests.append("Mohammad Hatta")

print("\nUndangan untuk semua tamu:")
for guest in guests:
    print(f"Halo {guest}, Anda diundang makan malam.")
