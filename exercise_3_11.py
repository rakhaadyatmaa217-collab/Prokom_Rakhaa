# Exercise 3-11: Intentional Error
# Bagian pertama sengaja meminta indeks yang tidak tersedia.
# Error ditangkap agar program tetap bisa dilanjutkan.

motorcycles = ["Honda", "Yamaha", "Suzuki"]

print("Daftar motor:", motorcycles)

try:
    print("Mencoba mengakses indeks ke-5:")
    print(motorcycles[5])  # Sengaja salah: indeks 5 tidak tersedia.
except IndexError:
    print("IndexError terjadi: indeks tersebut tidak tersedia.")

# Memperbaiki kesalahan dengan indeks yang benar.
print("\nSetelah diperbaiki:")
print(motorcycles[2])
