cities = {"Lagos", "Abuja", "Kaduna", "Jos", "Accra", "Dutse"}
print(cities)
cities.add("Ikeja")
print(cities)

cities.remove("Lagos")
# remove unexisting city with error
# cities.remove("Gombe")
# remove unexisting city without error
cities.discard("Gombe")
cities_clone = cities.copy()
print(cities_clone)
cities.clear()
print(cities)

# intersection, union and
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "John", "Matthew",
                    "Charles", "Charlotte", "Mesut", "James", "Olivet"}
# intersection
print(math_students.intersection(biology_students))
print(math_students & biology_students)
# union
print(math_students.union(biology_students))
print(math_students | biology_students)
