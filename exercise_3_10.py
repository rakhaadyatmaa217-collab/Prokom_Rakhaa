# Exercise 3-10: Every Function
# Contoh daftar band favorit dan penggunaan fungsi/metode list.

bands = ["Burgerkill", "Taring", "Revenge", "Seringai"]

# Mengakses elemen list
print("Band pertama:", bands[0])

# Mengubah elemen
bands[1] = "For Revenge"
print("Setelah mengubah elemen:", bands)

# Menambahkan elemen di akhir
bands.append("Beside")
print("Setelah append:", bands)

# Menambahkan elemen di posisi tertentu
bands.insert(1, "Voice of Baceprot")
print("Setelah insert:", bands)

# Menghapus berdasarkan posisi dengan del
del bands[2]
print("Setelah del:", bands)

# Menghapus elemen terakhir dengan pop
removed_band = bands.pop()
print(f"Band yang di-pop: {removed_band}")
print("Setelah pop:", bands)

# Menghapus berdasarkan nilai
bands.remove("Seringai")
print("Setelah remove:", bands)

# Mengurutkan list secara alfabetis
bands.sort()
print("Setelah sort:", bands)

# Menampilkan urutan alfabetis tanpa mengubah list asli
print("Hasil sorted:", sorted(bands))

# Membalik urutan list
bands.reverse()
print("Setelah reverse:", bands)

# Menghitung jumlah elemen
print("Jumlah band:", len(bands))
