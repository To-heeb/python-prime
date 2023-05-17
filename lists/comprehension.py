nums = [1, 2, 3]
name = "toheeb"
# list comprehension
# [__ for __ in __]

print([x*10 for x in nums])
print([char.upper() for char in name])
print([num*10 for num in range(1, 6)])
print([bool(val) for val in ['', 0, [], None, 1]])
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
with_vowel = "This is so much fun!"
print([num for num in numbers if num % 2 == 0])
print([num for num in numbers if num % 2 != 0])
print([num*2 if num % 2 != 0 else num/2 for num in numbers])
print(''.join(char for char in with_vowel if char not in "aeiou"))
