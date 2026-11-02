age = int(input("Masukkan umur: "))
if age < 2:
    stage = "bayi"
elif age < 4:
    stage = "balita"
elif age < 13:
    stage = "anak-anak"
elif age < 20:
    stage = "remaja"
elif age < 65:
    stage = "dewasa"
else:
    stage = "lanjut usia"
print(f"Kamu termasuk {stage}.")
