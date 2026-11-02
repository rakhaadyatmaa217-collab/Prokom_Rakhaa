# Versi 1: kondisi while
prompt = "Masukkan topping (quit untuk selesai): "
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Menambahkan {topping}.")

# Versi 2 dan 3 dapat memakai flag atau break seperti pola di bawah.
active = True
while active:
    answer = input("Ketik 'stop' untuk berhenti: ")
    if answer == "stop":
        active = False
