data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
colors = ["red", "green", "blue", "pink", "blue", "yellow"]
data.append("purple")
print(data)
data.extend(["red", "green", "blue", "pink", "blue", "yellow"])
print(data)
# at certain index
data.insert(9, 10)
print(data)
data.pop()
print(data)
data.pop(0)
print(data)
data.remove("pink")
print(data)
print(data.index("blue"))
print(data.index("blue", 5))
print(data.index("blue", 13, 14))
print(data.count("blue"))
print(data.count("green"))
data.reverse()
print(data)
colors.sort()
print(colors)

# slice
# list[start:end:step]
print(numbers[:])
print(numbers[1:])
print(numbers[:10])
print(numbers[5:15])
print(numbers[::2])
print(numbers[1::2])
print(colors[1][::-1])
data.clear()
print(data)
# ["read", "write", "update", "delete"]
#  == (used to compare values)
# is (used to compare objects in memory)
