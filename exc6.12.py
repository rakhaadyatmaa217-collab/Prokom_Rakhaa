# Ekstensi latihan: daftar user dan bahasa favorit dalam dictionary bersarang.
users = {
    "andi": {"language": "Python", "level": "beginner"},
    "siti": {"language": "Java", "level": "intermediate"},
    "budi": {"language": "Python", "level": "advanced"},
}
for username, details in users.items():
    print(
        f"{username.title()} studies {details['language']} "
        f"({details['level']})."
    )
