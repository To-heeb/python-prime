print("How old are you?")
age = input()

if not age == "":
    age = int(age)
     
    if age >= 18 and age < 21:
        print("You can enter but need a wrist band! ")
    elif age >= 21:
        print("You are good to enter and can drink! ")
    else:
        print("You can't enter little one! :(")
else:
    print("Please enter an age! ")

