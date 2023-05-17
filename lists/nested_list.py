coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

for loc in coords:
    for coord in loc:
        print(coord)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(item) for item in lizt] for lizt in nested_list]
[print(["X" if item % 2 != 0 else "O" for item in lizt])
 for lizt in nested_list]
