from random import randint


def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]


def capitalize(string):
    return string[0].upper() + string[1:]


def flip_coin():
    side = ""
    if randint(0, 1) == 0:
        side = "heads"
    else:
        side = "tails"
    return side


print(flip_coin())
