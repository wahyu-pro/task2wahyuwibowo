colors = ["red", "green", "yellow", "blue", "pink", "purple"]
patterns = ["dotted", "floral", "ditsy", "ikat", "stripes"]

colors.insert(2, "black")
del colors[3]
print(colors)
print(colors[1:5])

fabric = colors + patterns
print(fabric)