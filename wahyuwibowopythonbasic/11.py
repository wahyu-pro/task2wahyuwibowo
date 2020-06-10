for i in range(1, 1001):
    if (i % 2) == 1:
        if (i % 5) == 0:
            print(i, "Ganjil kelipatan 5")
        else:
            print(i, "Ganjil")
    elif (i % 2) == 0:
        if (i % 5) == 0:
            if (i % 100) == 0:
                print(i, "kelipatan 100")
            else:
                print(i, "Genap kelipatan 5")
        else:
            print(i, "Genap")