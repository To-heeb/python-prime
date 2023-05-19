# Parameter orders
# parameters
# *args
# default parameters
# **kwargs


# a - 1
# b - 2
# *args - (3,4,5)
# instructor - Toheeb
# **kwargs - {'last_name':"Oyekola", 'job':"Developer"}
def display_info(a, b, *args, instructor="Toheeb", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, 4, 5, last_name="Oyekola", job="Developer"))
