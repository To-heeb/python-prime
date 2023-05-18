instrutor = {
    "name": "Toheeb",
    "own_animal": False,
    "num_books": 1,
    "favorite_languages": ["english", "arabic", "yoruba", "hausa"],
    "is_funny": False,
    44: "Just another number"
}

letters = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13,
               n=14, o=15, p=16, q=17, r=18, s=19, t=20, u=21, v=22, w=23, x=24, y=25, z=26)
numbers = letters.copy()

print(letters)
new_users = {}.fromkeys(['name', 'email', 'score', 'profile_bio'], "unknown")
print(new_users)
print(new_users.get("name"))
new_users.pop("name")
print(new_users)
print(new_users.popitem())
new_users.update(letters)
print(new_users)
instrutor.update({"age": 45})
print(instrutor)
instrutor.clear()
print(instrutor)
