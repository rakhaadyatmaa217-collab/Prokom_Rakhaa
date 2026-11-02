prompt = "Masukkan topping pizza (ketik 'quit' untuk selesai): "
while True:
    topping = input(prompt)
    if topping.lower() == "quit":
        break
    print(f"Menambahkan {topping} ke pizza.")
