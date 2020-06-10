prime = list()

for x in range(100, 200):
    for a in range(2, x):
        if x % a == 0:
            break
    else:
        prime.append(x)
print(prime)