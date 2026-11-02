menu = ("fried rice", "soup", "noodles", "salad", "ice cream")
print("Menu awal:")
for food in menu:
    print(food)
# Percobaan mengubah tuple secara langsung akan menghasilkan TypeError.
# menu[0] = "steak"
menu = ("fried rice", "soup", "steak", "salad", "cake")
print("Menu baru:")
for food in menu:
    print(food)
