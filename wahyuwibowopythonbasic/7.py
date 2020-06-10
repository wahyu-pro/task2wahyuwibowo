number = int(input("Masukan Angka : "))

if number >= 90:
    print("A")
elif (number >= 80) and (number <= 89):
    print("B")
elif (number >= 70) and (number <= 79):
    print("C")
elif (number >= 60) and (number <= 69):
    print("D")
elif number <= 59:
    print("E")