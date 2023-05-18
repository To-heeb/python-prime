instrutor = {
    "name": "Toheeb",
    "own_animal": False,
    "num_books": 1,
    "favorite_languages": ["english", "arabic", "yoruba", "hausa"],
    "is_funny": False,
    44: "Just another number"
}

# order not assured in a dictionary
values = instrutor.values()
for value in values:
    print(value)

items = instrutor.items()
for item in items:
    print(item)

for key, value in items:
    print(f"{key} is {value}")

print(instrutor.values())
print(instrutor.keys())
print(instrutor.items())
print("name" in instrutor)
print("phone" in instrutor)
if (instrutor["name"]):
    print(instrutor["name"])
