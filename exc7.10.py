responses = {}
polling = True
while polling:
    name = input("Nama Anda: ")
    place = input("Ke mana Anda ingin berlibur? ")
    responses[name] = place
    repeat = input("Apakah orang lain ingin menjawab? (yes/no) ")
    if repeat.lower() != "yes":
        polling = False
print("\n--- Hasil polling ---")
for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")
