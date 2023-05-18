# list = [] or list()
# dict = {} or dict()
# tuple = () or tuple()
# set = {} or set()

# tuple are immutable
# tuple are faster than list
# tuple are used as keys in dictionaries

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(numbers))

for i in numbers:
    print(i)

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

for month in months:
    print(month)

locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7125, 74.6917): "New York Office",
    (42.3423, 145.6917): "Canada Office",
}
# numbers[0] = 0
