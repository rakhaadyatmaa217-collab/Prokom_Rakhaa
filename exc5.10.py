current_users = ["andi", "budi", "citra", "dewi", "eko"]
new_users = ["Budi", "fajar", "gina", "Andi", "hadi"]
current_lower = [name.lower() for name in current_users]

for new_user in new_users:
    if new_user.lower() in current_lower:
        print(f"{new_user} is already taken. Enter a new username.")
    else:
        print(f"{new_user} is available.")
