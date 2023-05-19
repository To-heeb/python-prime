# this gather all passed arguments as tuple
# *args

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(1, 2, 3, 4, 5, 6, 7, 8))


def ensure_correct_info(*info):
    if "Toheeb" in info and "Oyekola" in info:
        return "Welcome back Toheeb"
    return "Not sure hwo you are"


print(ensure_correct_info("Toheeb", "Oyekola"))
print(ensure_correct_info("Danladi", "Bako"))
