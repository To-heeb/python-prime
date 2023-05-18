numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print({number**2 for number in numbers})
print({number: number**2 for number in numbers})


def are_all_vowels_in_string(string):
    string = string.lower()
    return len({char for char in string if char in 'aeiou'}) == 5


print(are_all_vowels_in_string("sequoia"))
