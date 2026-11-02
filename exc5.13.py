# Contoh ide program menggunakan percabangan: menentukan diskon.
total_belanja = float(input("Total belanja (Rp): "))

if total_belanja >= 500_000:
    diskon = 0.20
elif total_belanja >= 250_000:
    diskon = 0.10
else:
    diskon = 0

potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

print(f"Diskon: Rp{potongan:,.0f}")
print(f"Total bayar: Rp{total_bayar:,.0f}")
