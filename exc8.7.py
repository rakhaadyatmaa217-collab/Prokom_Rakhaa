def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album


print(make_album("Tulus", "Monokrom"))
print(make_album("NOAH", "Second Chance"))
print(make_album("Adele", "30", 12))
