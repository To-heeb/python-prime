user_response = None

while user_response not in ["y", "n"]:
    user_response = input("Do you want to continue? (y/n): ")
    if user_response == "y":
        print("Installing ...............")
    elif user_response == "n":
        print("Failed to install")
