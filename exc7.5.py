prompt = "Masukkan umur (ketik 0 untuk selesai): "
while True:
    age = int(input(prompt))
    if age == 0:
        break
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"Harga tiket: ${price}")
