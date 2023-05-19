# this gather all passed keyword and values arguments as a dictionary
# **kwargs


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favourite color is {color}")


fav_colors(toheeb='red', abike='blue', habib='green', eniola='yellow')
