rateFilm = int(input("Masukan umur anda ! "))


if rateFilm >= 21:
    print("DEWASA")
elif rateFilm >= 13:
    print("REMAJA")
elif rateFilm >= 9:
    print("BIMBINGAN ORANG TUA")
elif rateFilm < 9:
    print("SEMUA USIA")