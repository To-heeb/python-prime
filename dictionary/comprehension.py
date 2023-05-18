# {__:__ for__ in __}

numbers = dict(first=1, second=2, third=3, fourth=4, fifth=5, sixth=6)
squared_number = {key: value ** 2 for key, value in numbers.items()}
print(squared_number)

str1 = "ABC"
str2 = "123"
combine = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combine)
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

even_odd = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(even_odd)
print({key.upper(): values * 2 for key, values in numbers.items()})
