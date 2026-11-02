# Contoh penggunaan fungsi dari modul terpisah.
# Simpan fungsi berikut sebagai module_greetings.py:
# def greet_user(name):
#     print(f"Hello, {name.title()}!")
#
# Lalu simpan file ini dan module_greetings.py dalam folder yang sama.
# Aktifkan dua baris berikut setelah file modul dibuat:
# from module_greetings import greet_user
# greet_user("sarah")

def greet_user(name):
    print(f"Hello, {name.title()}!")


greet_user("sarah")
