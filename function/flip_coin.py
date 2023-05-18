from random import randint


def flip_coin():
    side = ""
    if randint(0, 1) == 0:
        side = "heads"
    else:
        side = "tails"
    return side


print(flip_coin())
