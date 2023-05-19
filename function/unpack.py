

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
nums_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

# * unpacks lists and tuples

print(*num_list)
print(sum_all_nums(*num_list))

print(*nums_tuple)
print(sum_all_nums(*nums_tuple))

# unpacks dictionaries


def letter_nums(a, b, c):
    print(a, b, c)


d = {'a': 1, 'b': 2, 'c': 3}

print(*d)
letter_nums(**d)


def add_and_multiply(a, b, c, **kwargs):
    print(a + b * c)
    print("===========")
    print(kwargs)


data = dict(a=1, b=2, c=3, d="dict", e="element")
add_and_multiply(**data)
